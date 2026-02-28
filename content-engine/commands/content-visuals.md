---
description: Generate image prompts and visuals for blog articles
allowed-tools: Read, Write, Glob, Grep, Bash(curl:*, jq:*, base64:*, wc:*, uname:*, file:*, mkdir:*, date:*, rm:*, mktemp:*, head:*, cat:*, dirname:*, tr:*, grep:*)
---

# Content Visuals

Generate brand-aware image prompts and visuals for blog articles, with optional Gemini-powered image generation.

## Usage

```
/content-visuals <article-path> [options]
```

## Options

| Flag | Values | Description |
|------|--------|-------------|
| `--style` | Any of 9 styles | Override auto-selected art style |
| `--mood` | `professional`, `energetic`, `warm` | Override auto-selected mood |
| `--preset` | `standard`, `data-vis`, `friendly`, etc. | Style+mood shortcut |
| `--types` | `cover`, `facebook`, `instagram` (comma-separated) | Which image types to generate |
| `--model` | `flash`, `pro` | Gemini model tier (default: `flash`) |
| `--quick` | — | Skip confirmation prompt |

## Execution

This command routes to the `content-visuals` skill. Follow the full workflow defined in `skills/content-visuals/SKILL.md`.

### Model Flag Handling

When `--model` is provided:
- `flash` → use `gemini-2.5-flash-image` (fast, default)
- `pro` → use `gemini-3-pro-image-preview` (quality, 4K)

If `--model` is omitted, default to `flash`.

The model flag only applies when the backend in `config/image-generation.json` is set to `gemini`. For `prompt-only` or other backends, the flag is ignored.
