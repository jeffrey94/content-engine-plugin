# WhatsApp Summarizer

A Cowork plugin that transcribes WhatsApp voice messages and photos using Gemini, then summarizes conversations with Claude.

## Setup

### API Key

Set `GEMINI_API_KEY` as a shell environment variable:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Add it to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.) for persistence.

### Dependencies

The script uses `uv` to manage dependencies automatically. No manual install needed. Required packages:

- `google-genai` — Google Gemini API client

## Commands

### `/transcribe-chat <folder-path>`

Transcribes a WhatsApp chat export. Voice messages are transcribed and photos are described using Gemini.

1. Reads `_chat.txt` from the provided folder
2. Shows a date/activity preview
3. Asks you to confirm the date range (or trim it)
4. Runs Gemini transcription on all voice messages and photos
5. Saves `transcription.md` alongside the input files

### `/clarify-chat <folder-path>`

Asks you clarifying questions about the transcribed conversation to build context for a better summary.

1. Reads `transcription.md` from the folder
2. Asks about participants, context, important topics, and desired outcomes
3. Saves your answers to `context.md`

### `/summarize-chat <folder-path>`

Generates a structured summary of the conversation in English.

1. Reads `transcription.md` and `context.md` (if available)
2. Produces a summary with: Key Topics, Decisions Made, Action Items, Notable References
3. Saves `summary.md` to the same folder

## Typical Workflow

```bash
# 1. Export a WhatsApp chat (include media) and unzip it

# 2. Transcribe voice messages and photos
/transcribe-chat ~/Downloads/WhatsApp\ Chat\ -\ Someone/

# 3. (Optional) Add context for a better summary
/clarify-chat ~/Downloads/WhatsApp\ Chat\ -\ Someone/

# 4. Generate the summary
/summarize-chat ~/Downloads/WhatsApp\ Chat\ -\ Someone/
```

## Output Files

All output is written alongside the original WhatsApp export:

```
WhatsApp Chat - Someone/
├── _chat.txt            (original export)
├── *.opus               (original voice messages)
├── transcription.md     (from /transcribe-chat)
├── context.md           (from /clarify-chat)
└── summary.md           (from /summarize-chat)
```
