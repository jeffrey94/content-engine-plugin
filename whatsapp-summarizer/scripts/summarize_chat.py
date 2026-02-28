#!/usr/bin/env python3
"""
WhatsApp Chat Transcriber

Parses a WhatsApp exported chat folder, transcribes voice messages
and describes photos using Gemini Flash, then assembles a
chronological transcription markdown file.

Usage:
    python summarize_chat.py <path_to_whatsapp_export_folder> [options]

Options:
    --start-date YYYY-MM-DD   Only include messages from this date
    --end-date YYYY-MM-DD     Only include messages up to this date
    --output-dir PATH         Write transcription.md to this directory (default: same as input)
"""

import argparse
import asyncio
import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path

from google import genai
from google.genai import types

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Message:
    timestamp: datetime
    sender: str
    content_type: str  # "text", "audio", "photo", "system"
    text: str | None = None
    file_path: Path | None = None
    transcription: str | None = None


# ---------------------------------------------------------------------------
# Chat parser
# ---------------------------------------------------------------------------

# WhatsApp export format: [DD/MM/YYYY, HH:MM:SS AM/PM] Sender: message
LINE_RE = re.compile(
    r"^\[(\d{2}/\d{2}/\d{4},\s*\d{1,2}:\d{2}:\d{2}\s*[AP]M)\]\s+(.+?):\s(.+)$"
)
ATTACHMENT_RE = re.compile(r"<attached:\s*(.+?)>")
TIMESTAMP_FMT = "%d/%m/%Y, %I:%M:%S %p"


def parse_chat(chat_dir: Path) -> list[Message]:
    """Parse _chat.txt and return a list of Message objects."""
    chat_file = chat_dir / "_chat.txt"
    if not chat_file.exists():
        raise FileNotFoundError(f"No _chat.txt found in {chat_dir}")

    messages: list[Message] = []
    raw = chat_file.read_text(encoding="utf-8")

    for line in raw.splitlines():
        # Strip invisible Unicode characters (BOM, LTR marks, etc.)
        line = line.strip("\ufeff\u200e\u200f\u202a\u202c\u200b")
        match = LINE_RE.match(line)
        if not match:
            continue

        ts_str, sender, body = match.groups()
        ts = datetime.strptime(ts_str, TIMESTAMP_FMT)
        body = body.strip("\u200e\u200f ")

        # Check for attachment
        att_match = ATTACHMENT_RE.search(body)
        if att_match:
            filename = att_match.group(1)
            file_path = chat_dir / filename
            if filename.lower().endswith((".opus", ".ogg", ".m4a", ".mp3", ".wav")):
                content_type = "audio"
            elif filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                content_type = "photo"
            else:
                content_type = "text"
                file_path = None
            messages.append(Message(
                timestamp=ts,
                sender=sender,
                content_type=content_type,
                file_path=file_path,
            ))
        elif body.startswith("\u200e"):
            # System message (security code change, etc.)
            messages.append(Message(
                timestamp=ts, sender=sender,
                content_type="system", text=body.strip("\u200e "),
            ))
        else:
            messages.append(Message(
                timestamp=ts, sender=sender,
                content_type="text", text=body,
            ))

    return messages


def filter_by_date(
    messages: list[Message],
    start_date: date | None,
    end_date: date | None,
) -> list[Message]:
    """Filter messages to only include those within the date range."""
    filtered = messages
    if start_date:
        filtered = [m for m in filtered if m.timestamp.date() >= start_date]
    if end_date:
        filtered = [m for m in filtered if m.timestamp.date() <= end_date]
    return filtered


# ---------------------------------------------------------------------------
# Gemini transcription / vision
# ---------------------------------------------------------------------------

AUDIO_MIME = {
    ".opus": "audio/ogg",
    ".ogg": "audio/ogg",
    ".m4a": "audio/mp4",
    ".mp3": "audio/mpeg",
    ".wav": "audio/wav",
}

PHOTO_MIME = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".webp": "image/webp",
}

TRANSCRIBE_PROMPT = (
    "Transcribe this voice message verbatim. "
    "The speaker uses a mix of Mandarin Chinese and English — "
    "preserve the original language as spoken. "
    "Do NOT translate. Output only the transcription, nothing else."
)

DESCRIBE_PHOTO_PROMPT = (
    "Describe what is shown in this image in 1-3 sentences. "
    "Be concise and factual."
)


async def process_media(
    client: genai.Client,
    messages: list[Message],
    model: str = "gemini-3-flash-preview",
    concurrency: int = 5,
) -> None:
    """Transcribe audio and describe photos in-place on Message objects."""
    semaphore = asyncio.Semaphore(concurrency)

    async def handle(msg: Message) -> None:
        async with semaphore:
            if msg.file_path is None or not msg.file_path.exists():
                msg.transcription = "[File not found]"
                return

            data = msg.file_path.read_bytes()
            ext = msg.file_path.suffix.lower()

            if msg.content_type == "audio":
                mime = AUDIO_MIME.get(ext, "audio/ogg")
                prompt = TRANSCRIBE_PROMPT
            elif msg.content_type == "photo":
                mime = PHOTO_MIME.get(ext, "image/jpeg")
                prompt = DESCRIBE_PHOTO_PROMPT
            else:
                return

            try:
                response = await asyncio.to_thread(
                    client.models.generate_content,
                    model=model,
                    contents=[
                        types.Part.from_bytes(data=data, mime_type=mime),
                        prompt,
                    ],
                )
                msg.transcription = response.text.strip()
            except Exception as e:
                msg.transcription = f"[Transcription error: {e}]"

    media_msgs = [m for m in messages if m.content_type in ("audio", "photo")]
    print(f"Processing {len(media_msgs)} media files with Gemini...", file=sys.stderr)

    tasks = [asyncio.create_task(handle(m)) for m in media_msgs]
    for i, task in enumerate(asyncio.as_completed(tasks), 1):
        await task
        print(f"  [{i}/{len(media_msgs)}] done", file=sys.stderr)


# ---------------------------------------------------------------------------
# Output assembly
# ---------------------------------------------------------------------------

ICON = {"text": "\U0001f4ac", "audio": "\U0001f3a4", "photo": "\U0001f4f7", "system": "\u2139\ufe0f"}


def assemble_transcription(messages: list[Message], chat_dir: Path) -> str:
    """Build the transcription markdown string."""
    senders = sorted({m.sender for m in messages if m.content_type != "system"})
    folder_name = chat_dir.name

    dates = [m.timestamp for m in messages]
    date_start = min(dates).strftime("%Y-%m-%d")
    date_end = max(dates).strftime("%Y-%m-%d")
    generated = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines: list[str] = []
    lines.append(f"# WhatsApp Chat Transcription: {' & '.join(senders)}")
    lines.append(f"**Source:** {folder_name}")
    lines.append(f"**Date range:** {date_start} to {date_end}")
    lines.append(f"**Generated:** {generated}")
    lines.append("")
    lines.append("---")
    lines.append("")

    current_date = None
    for msg in messages:
        msg_date = msg.timestamp.strftime("%Y-%m-%d")
        if msg_date != current_date:
            current_date = msg_date
            lines.append(f"## {current_date}")
            lines.append("")

        time_str = msg.timestamp.strftime("%H:%M")
        icon = ICON.get(msg.content_type, "")

        if msg.content_type == "system":
            lines.append(f"*[{time_str}] {msg.text}*")
            lines.append("")
            continue

        lines.append(f"**[{time_str}] {msg.sender}** {icon}:")

        if msg.content_type == "text":
            lines.append(f"> {msg.text}")
        elif msg.content_type == "audio":
            text = msg.transcription or "[Not transcribed]"
            lines.append(f"> {text}")
        elif msg.content_type == "photo":
            desc = msg.transcription or "[No description]"
            lines.append(f"> [Photo: {desc}]")

        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def build_summary(messages: list[Message], chat_dir: Path, output_path: Path) -> dict:
    """Build a JSON-serializable summary of the transcription run."""
    dates = [m.timestamp for m in messages]
    type_counts = {}
    for m in messages:
        type_counts[m.content_type] = type_counts.get(m.content_type, 0) + 1

    return {
        "chat_name": chat_dir.name,
        "total_messages": len(messages),
        "message_types": type_counts,
        "date_start": min(dates).strftime("%Y-%m-%d"),
        "date_end": max(dates).strftime("%Y-%m-%d"),
        "output_path": str(output_path),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="WhatsApp Chat Transcriber")
    parser.add_argument("chat_dir", help="Path to WhatsApp export folder containing _chat.txt")
    parser.add_argument("--start-date", help="Only include messages from this date (YYYY-MM-DD)")
    parser.add_argument("--end-date", help="Only include messages up to this date (YYYY-MM-DD)")
    parser.add_argument("--output-dir", help="Directory to write transcription.md (default: same as chat_dir)")
    return parser.parse_args()


async def main() -> None:
    args = parse_args()

    chat_dir = Path(args.chat_dir).resolve()

    # Find _chat.txt — either directly in chat_dir or in a subfolder
    if not (chat_dir / "_chat.txt").exists():
        # Check one level of subdirectories
        found = None
        if chat_dir.is_dir():
            for child in sorted(chat_dir.iterdir()):
                if child.is_dir() and (child / "_chat.txt").exists():
                    found = child
                    break
        if found:
            chat_dir = found
        else:
            print(f"Error: No _chat.txt found in {chat_dir}", file=sys.stderr)
            sys.exit(1)

    # Parse date filters
    start_date = None
    end_date = None
    if args.start_date:
        start_date = date.fromisoformat(args.start_date)
    if args.end_date:
        end_date = date.fromisoformat(args.end_date)

    # Output directory
    output_dir = Path(args.output_dir).resolve() if args.output_dir else chat_dir

    # API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not set in environment.", file=sys.stderr)
        sys.exit(1)

    # Parse
    print(f"Parsing chat from: {chat_dir}", file=sys.stderr)
    messages = parse_chat(chat_dir)
    print(f"Found {len(messages)} total messages", file=sys.stderr)

    # Filter by date
    messages = filter_by_date(messages, start_date, end_date)
    if not messages:
        print("Error: No messages in the specified date range.", file=sys.stderr)
        sys.exit(1)
    print(f"After date filter: {len(messages)} messages", file=sys.stderr)

    # Transcribe media
    client = genai.Client(api_key=api_key)
    await process_media(client, messages)

    # Assemble and write transcription
    transcription_md = assemble_transcription(messages, chat_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "transcription.md"
    output_path.write_text(transcription_md, encoding="utf-8")
    print(f"Transcription saved to: {output_path}", file=sys.stderr)

    # Print JSON summary to stdout for the command to parse
    summary = build_summary(messages, chat_dir, output_path)
    print(json.dumps(summary))


if __name__ == "__main__":
    asyncio.run(main())
