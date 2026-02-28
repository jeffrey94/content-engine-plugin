---
name: clarify-chat
description: Ask clarifying questions about a transcribed chat to build context for summarization
allowed-tools: Read, Write, AskUserQuestion
---

# Clarify Chat Context

You are helping the user build context around a transcribed WhatsApp conversation so that the subsequent summary is accurate and useful.

## Input

The user provides `$ARGUMENTS` — a path to a folder containing `transcription.md` (produced by `/transcribe-chat`).

## Steps

### 1. Load the transcription

Read `transcription.md` from the provided folder path. If the file doesn't exist, tell the user to run `/transcribe-chat` first.

### 2. Analyze the conversation

Read through the transcription and identify:
- Who the participants are
- The apparent topics and themes
- Any decisions, plans, or action items mentioned
- The language(s) used
- The apparent relationship (business, personal, etc.)

### 3. Ask clarifying questions

Use the AskUserQuestion tool to ask the user these questions **one at a time** (or in small groups of 2 if related):

1. **Who are the parties?** "I see messages between [names]. Can you tell me who they are and their roles? (e.g., 'Marcus is my business partner', 'I'm Jeffrey')"

2. **What's the context?** "What's the relationship or context for this conversation? (e.g., business collaboration, project planning, personal)"

3. **What matters most?** "Which topics or themes are most important to you in this conversation? Anything I should pay special attention to?"

4. **Action items?** "Are there specific outcomes, decisions, or action items you want highlighted in the summary?"

5. **Anything else?** "Any other context that would help me write a better summary? (e.g., background on projects mentioned, acronyms used)"

Adapt your questions based on what you see in the transcription. Skip questions that are obvious from context. Add questions if you notice ambiguous references or unclear topics.

### 4. Save context

Compile the user's answers into `context.md` in the same folder. Format:

```markdown
# Chat Context

## Participants
- [Name]: [Role/description as provided by user]
- [Name]: [Role/description]

## Relationship / Setting
[User's description of the context]

## Key Topics to Highlight
[What the user said matters most]

## Desired Outcomes
[Action items, decisions, or other things to emphasize]

## Additional Context
[Any other notes from the user]
```

Write `context.md` to the same folder as `transcription.md`.

Tell the user that context has been saved and they can now run `/summarize-chat` on the same folder.
