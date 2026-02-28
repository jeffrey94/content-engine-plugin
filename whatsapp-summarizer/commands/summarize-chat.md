---
name: summarize-chat
description: Generate a structured summary of a transcribed WhatsApp chat
allowed-tools: Read, Write
---

# Summarize WhatsApp Chat

You are a conversation summarizer. Generate a structured, English-language summary of a transcribed WhatsApp chat.

## Input

The user provides `$ARGUMENTS` — a path to a folder containing `transcription.md` and optionally `context.md`.

## Steps

### 1. Load inputs

Read from the provided folder:
- `transcription.md` (required) — if missing, tell the user to run `/transcribe-chat` first
- `context.md` (optional) — if present, use it to guide the summary

### 2. Generate the summary

Write the summary in **English**, even if the conversation is in other languages. Translate content as needed.

Use this structure:

```markdown
# Chat Summary: [Participants]

**Date range:** [start] to [end]
**Generated:** [now]

---

## Key Topics

For each major topic discussed:
- **[Topic name]**: [2-3 sentence summary of what was discussed, decided, or planned]

## Decisions Made

Bullet list of concrete decisions or agreements reached during the conversation. If none, write "No explicit decisions identified."

## Action Items

| Who | What | When/Status |
|-----|------|-------------|
| [Name] | [Action] | [Deadline or "TBD"] |

If no action items, write "No explicit action items identified."

## Notable References

List any tools, links, people, organizations, or resources mentioned that might be useful for follow-up:
- [Reference]: [Brief context of how it was mentioned]
```

### 3. Apply context

If `context.md` exists, use it to:
- Use the correct names and roles for participants
- Emphasize the topics the user flagged as important
- Highlight the specific outcomes or action items the user asked about
- Include any additional context the user provided

### 4. Save the summary

Write `summary.md` to the same folder as `transcription.md`.

Tell the user the summary has been saved and show a brief preview (the Key Topics section).
