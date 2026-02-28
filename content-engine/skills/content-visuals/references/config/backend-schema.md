# Image Generation Backend Schema

## Purpose

Documents the structure and fields of `config/image-generation.json`, which controls the pluggable image generation backend.

## File Location

`config/image-generation.json` (relative to project root)

## Top-Level Fields

| Field | Type | Description |
|---|---|---|
| `backend` | string | Active backend ID. One of: `prompt-only`, `gemini`. |
| `backends` | object | Backend definitions. Each key is a backend ID. |
| `fallback_behavior` | string | What to do when active backend fails. |
| `output_directory_pattern` | string | Output path pattern with `YYYYMMDD` and `{article-slug}` placeholders. |

## Backend Definition Fields

Each backend object under `backends` has:

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string | Yes | Human-readable description. |
| `enabled` | boolean | Yes | Whether this backend is available for use. |
| `api_key_env` | string | No | Environment variable name containing the API key. Not needed for `prompt-only`. |
| `model` | string | No | Model identifier for API calls. |
| `max_images_per_run` | integer | No | Rate limit guard. Default: 10. |
| `output_format` | string | No | Image format: `png`, `webp`, `jpg`. Default: `png`. |
| `models` | object | No | Model tier definitions (e.g., `flash`, `pro`) with `id`, `description`, `tier` fields. |
| `output` | string | No | Special output mode (e.g., `prompts-only` for prompt-only backend). |

## How Backends Are Used

### prompt-only (Default)
- No API calls made
- Prompt files are saved to `prompts/` directory
- User can manually paste prompts into any image generation tool
- Always works, no dependencies

### gemini
- Calls Google Gemini API for image generation via `curl`
- Requires `GEMINI_API_KEY` in environment
- Uses model specified in config (default: `gemini-2.5-flash-image`)
- Supports `flash` and `pro` model tiers via `--model` flag
- See `references/backends/gemini.md` for full implementation details

## Switching Backends

To switch backends, edit `config/image-generation.json`:

1. Set `"backend"` to the desired backend ID
2. Ensure the backend's `"enabled"` is `true`
3. If API backend: set the API key in your `.env` file
4. Run the skill -- it will use the new backend

## Fallback Behavior

If the active backend fails (API error, missing key, rate limit):

1. Log the error with details
2. Fall back to `prompt-only` mode
3. Notify user: "Backend {name} failed: {reason}. Prompts saved to {path}. Switch to prompt-only mode."
4. Continue workflow -- prompts are always saved regardless of backend
