---
name: content-visuals
description: >
  Generate image prompts and visuals for blog articles. Use when the user asks to
  "create images for an article", "generate blog visuals", "make a cover image",
  "create social media cards", "/content-visuals", or needs image prompts for
  cover heroes, Facebook cards, or Instagram cards matching article content.
version: 0.2.0
---

# Content Visuals

Generate brand-aware image prompts and visuals for blog articles. Supports 9 art styles, 3 moods, 3 image types, and pluggable generation backends.

## Quick Start

Provide an article path and optional overrides:

```
/content-visuals path/to/article.md
/content-visuals path/to/article.md --style bold-graphic --mood energetic
/content-visuals path/to/article.md --preset data-vis
/content-visuals path/to/article.md --quick
/content-visuals path/to/article.md --types cover,instagram
/content-visuals path/to/article.md --model flash
/content-visuals path/to/article.md --model pro --types cover
```

## Three Dimensions

### Styles (9 available)

| Style | Best For |
|-------|----------|
| `flat-vector` | Clean geometric — Policy & Compliance |
| `isometric` | 2.5D technical — Infrastructure, supply chains |
| `hand-drawn` | Sketch-like — Practical guides, how-to |
| `corporate-modern` | Polished gradient — Most blog posts (default) |
| `bold-graphic` | High contrast — Urgent news, deadlines |
| `watercolor` | Soft organic — Success stories, community |
| `minimal-line` | Single-weight premium — Executive content |
| `data-visual` | Chart-inspired — Statistics-heavy articles |
| `cultural-motif` | Local patterns — Culturally-themed topics |

### Moods (3 available)
- `professional` — corporate, trustworthy, clean
- `energetic` — vibrant, dynamic, action-oriented
- `warm` — friendly, approachable, community-focused

### Image Types (3 available)

| Type | Dimensions | Aspect Ratio |
|------|-----------|--------------|
| `cover-hero` | 1200 x 675 px | 16:9 |
| `facebook-card` | 1200 x 628 px | 1.91:1 |
| `instagram-card` | 1080 x 1080 px (or 1080 x 1350 px carousel) | 1:1 or 4:5 |

## Auto-Selection

When no style is specified, match based on content pillar:

| Content Pillar | Style | Mood |
|----------------|-------|------|
| Policy & Compliance | corporate-modern | professional |
| Funding & Financing | data-visual | professional |
| Industry Opportunities | isometric | energetic |
| Practical Guides | hand-drawn | warm |

## Presets

Shortcut combinations:

| Preset | Style + Mood |
|--------|-------------|
| `standard` | corporate-modern + professional |
| `data-vis` | data-visual + professional |
| `friendly` | hand-drawn + warm |
| `impact` | bold-graphic + energetic |
| `cultural` | cultural-motif + warm |
| `clean` | minimal-line + professional |
| `tech` | isometric + professional |
| `creative` | watercolor + warm |
| `flat` | flat-vector + professional |

## Compatibility Matrix

`++` recommended, `+` works, `-` avoid:

| Style | Professional | Energetic | Warm |
|-------|-------------|-----------|------|
| flat-vector | ++ | + | + |
| isometric | ++ | ++ | - |
| hand-drawn | + | + | ++ |
| corporate-modern | ++ | + | - |
| bold-graphic | + | ++ | - |
| watercolor | - | - | ++ |
| minimal-line | ++ | - | + |
| data-visual | ++ | + | - |
| cultural-motif | + | - | ++ |

## Brand Integration

Load brand colors and typography from `config/brands/_active.json` → points to the active brand file in `config/brands/`. Use the brand's palette to tint generated visuals.

## Workflow

1. **Read article** — parse frontmatter, extract key statistics, identify content pillar
2. **Auto-select style** — match pillar to style+mood (or use overrides)
3. **Confirm with user** (unless `--quick`) — present recommendation, wait for approval
4. **Ask image count** — how many of each type?
5. **Generate prompts** — assemble 4-layer prompt: type template + style rules + brand palette + article context
6. **Generate images** (if backend configured) — see sub-steps below
7. **Save output** — prompts and images to `data/images/YYYYMMDD/{article-slug}/`

### Step 6: Image Generation Details

#### 6a. Check Environment

Determine which backend is configured in `config/image-generation.json`.

**If backend is `prompt-only`:**
Skip generation. Prompts are already saved from Step 5.

**If backend is `gemini`:**

1. Check if `$GEMINI_API_KEY` is set in the environment
2. If **missing**, tell the user:
   > "Image generation requires a Gemini API key. Your prompts have been saved to `data/images/...` — you can copy them into [Google AI Studio](https://aistudio.google.com) or any image generation tool to create your images. To enable automatic generation in Claude Code, set `GEMINI_API_KEY` in your `.env` file."
3. If **present**, proceed to 6b

**If backend is any other value:**
Fall back to prompt-only and notify the user that the backend is not yet implemented.

#### 6b. Select Model

Resolve the model ID from the `--model` flag:
- `--model flash` → `gemini-2.5-flash-image` (default if no flag)
- `--model pro` → `gemini-3-pro-image-preview`

Read model config from `config/image-generation.json` → `backends.gemini.models`.

#### 6c. Generate Each Image

For each prompt file saved in Step 5, follow the procedure in `references/backends/gemini.md`:

1. Read the prompt markdown file (strip YAML frontmatter, use only the prompt body)
2. Build JSON payload with `jq` → temp file
3. Call the Gemini API via `curl`
4. Extract base64 image data with `jq`
5. Decode to PNG with `base64` (platform-aware decode flag)
6. Validate file size with `wc -c`
7. Save to `data/images/YYYYMMDD/{article-slug}/generated/{type}-{N}.png`
8. Clean up temp files

#### 6d. Handle Results

**On success:**
Report each generated image with file path and size:
> "Generated cover-hero.png (245,832 bytes)"

**On failure (per image):**
1. Log the error in the manifest
2. Confirm the prompt file is saved and available
3. Suggest the user can paste the prompt into [Google AI Studio](https://aistudio.google.com) manually
4. Continue generating remaining images — do not abort the batch

**On total failure (API key invalid, all requests fail):**
1. Confirm all prompts are saved
2. Suggest manual generation path
3. Update manifest with error status

## Output Structure

```
data/images/YYYYMMDD/{article-slug}/
  prompts/
    cover-hero-prompt.md
    facebook-card-1-prompt.md
    instagram-card-1-prompt.md
  generated/          (only when API backend is active)
    *.png
  manifest.json
```

## Image Generation Backend

Load from `config/image-generation.json`. Available backends:
- `prompt-only` (default) — saves prompts only, no API calls
- `gemini` — Google Gemini (requires `GEMINI_API_KEY`)

If the selected backend fails or the API key is missing, fall back to `prompt-only` mode.

## References

Detailed specifications for each dimension:
- `references/styles/*.md` — full style definitions for each of the 9 styles
- `references/image-types/*.md` — specs for cover-hero, facebook-card, instagram-card
- `references/base-prompt.md` — 4-layer prompt assembly guide
- `references/auto-selection.md` — content signal → style mapping
- `references/compatibility.md` — style × mood and style × image-type matrices
- `references/style-presets.md` — preset shortcut definitions
- `references/visual-elements.md` — universal visual rules
- `references/workflow/*.md` — step-by-step workflow procedures
- `references/config/*.md` — backend and preferences schemas
- `references/backends/gemini.md` — Gemini API curl implementation reference
