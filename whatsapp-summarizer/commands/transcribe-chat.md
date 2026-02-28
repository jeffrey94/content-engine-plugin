---
name: transcribe-chat
description: Transcribe a WhatsApp chat export — voice messages and photos processed via Gemini
allowed-tools: Bash, Read, Write, AskUserQuestion
---

# Transcribe WhatsApp Chat

You are a WhatsApp chat transcription assistant. The user wants to transcribe a WhatsApp chat export, including voice messages and photos, using Gemini.

## Input

The user provides `$ARGUMENTS` — a path to a folder containing a WhatsApp export (with `_chat.txt` and media files).

## Steps

### 1. Locate the chat

Resolve the folder path from `$ARGUMENTS`. Look for `_chat.txt` either directly in the folder or one level down in a subfolder.

If `_chat.txt` is not found, tell the user and stop.

### 2. Parse and preview

Read `_chat.txt` and parse it to show the user a preview. Use a Bash command to do a quick analysis:

```bash
python3 -c "
import re, sys
from collections import Counter, defaultdict
from pathlib import Path

chat_dir = Path('$ARGUMENTS').resolve()
# Find _chat.txt
chat_file = chat_dir / '_chat.txt'
if not chat_file.exists():
    for child in sorted(chat_dir.iterdir()):
        if child.is_dir() and (child / '_chat.txt').exists():
            chat_file = child / '_chat.txt'
            chat_dir = child
            break

if not chat_file.exists():
    print('ERROR: No _chat.txt found')
    sys.exit(1)

raw = chat_file.read_text(encoding='utf-8')
LINE_RE = re.compile(r'^\[(\d{2}/\d{2}/\d{4},\s*\d{1,2}:\d{2}:\d{2}\s*[AP]M)\]\s+(.+?):\s(.+)$')
ATT_RE = re.compile(r'<attached:\s*(.+?)>')

dates = defaultdict(lambda: Counter())
senders = set()
total = 0

for line in raw.splitlines():
    line = line.strip('\ufeff\u200e\u200f\u202a\u202c\u200b')
    m = LINE_RE.match(line)
    if not m:
        continue
    ts_str, sender, body = m.groups()
    day = ts_str.split(',')[0]  # DD/MM/YYYY
    # Convert to YYYY-MM-DD
    parts = day.strip().split('/')
    iso_date = f'{parts[2]}-{parts[1]}-{parts[0]}'
    senders.add(sender)
    total += 1

    att = ATT_RE.search(body)
    if att:
        fname = att.group(1).lower()
        if fname.endswith(('.opus','.ogg','.m4a','.mp3','.wav')):
            dates[iso_date]['voice'] += 1
        elif fname.endswith(('.jpg','.jpeg','.png','.webp')):
            dates[iso_date]['photo'] += 1
        else:
            dates[iso_date]['text'] += 1
    else:
        dates[iso_date]['text'] += 1

all_voice = sum(d['voice'] for d in dates.values())
all_photo = sum(d['photo'] for d in dates.values())
all_text = sum(d['text'] for d in dates.values())
sorted_dates = sorted(dates.keys())

print(f'Found: {chat_dir.name}')
print(f'Date range: {sorted_dates[0]} to {sorted_dates[-1]}')
print(f'Total: {total} messages ({all_voice} voice, {all_photo} photos, {all_text} text)')
print()
print('Activity by date:')
for d in sorted_dates:
    c = dates[d]
    parts = []
    if c['voice']: parts.append(f\"{c['voice']} voice\")
    if c['photo']: parts.append(f\"{c['photo']} photo\")
    if c['text']: parts.append(f\"{c['text']} text\")
    print(f'  {d}: {sum(c.values())} messages ({', '.join(parts)})')
"
```

Display the output to the user.

### 3. Confirm date range

Ask the user:
- Do they want to transcribe the **full date range**, or
- Do they want to specify a **start date** and/or **end date** to trim?

Use the AskUserQuestion tool with options like:
- "Full range" (recommended)
- "Specify date range"

If they choose to specify, ask for start and end dates.

### 4. Run the transcription script

Determine the plugin's script location. The script is at the path relative to this command file: `../scripts/summarize_chat.py`.

Run the script:

```bash
SCRIPT_DIR="$(cd "$(dirname "$0")/../scripts" 2>/dev/null && pwd || echo "scripts")"
uv run --with google-genai python3 "$SCRIPT_DIR/summarize_chat.py" "<chat_folder_path>" [--start-date YYYY-MM-DD] [--end-date YYYY-MM-DD] [--output-dir "<chat_folder_path>"]
```

The `--output-dir` should be set to the same folder as the chat export so `transcription.md` is saved alongside the original files.

Progress output goes to stderr; the final line on stdout is a JSON summary.

### 5. Report results

Parse the JSON summary from stdout and tell the user:
- How many messages were transcribed
- How many voice/photo/text messages
- Where `transcription.md` was saved

If there were any transcription errors, mention them.
