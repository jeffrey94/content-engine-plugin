---
name: content-visuals
description: >
  Generate image prompts and visuals for blog articles. Use when the user asks to
  "create images for an article", "generate blog visuals", "make a cover image",
  "create social media cards", "/content-visuals", or needs image prompts for
  cover heroes, Facebook cards, or Instagram cards matching article content.
version: 0.1.0
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
6. **Generate images** (if backend configured) — call the active backend from `config/image-generation.json`
7. **Save output** — prompts and images to `data/images/YYYYMMDD/{article-slug}/`

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
- `claude` — Claude's built-in image generation
- `gemini` — Google Gemini (requires `GEMINI_API_KEY`)
- `dall-e` — OpenAI DALL-E (requires `OPENAI_API_KEY`)
- `stable-diffusion` — Stability AI (requires `STABILITY_API_KEY`)

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
