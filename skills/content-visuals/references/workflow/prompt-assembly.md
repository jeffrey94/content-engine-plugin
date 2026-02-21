# Prompt Assembly Procedure

## Purpose

Step-by-step procedure for assembling image generation prompts in Step 5 of the workflow. References `base-prompt.md` for the template structure.

## Prerequisites

Before prompt assembly, you must have:
- Article analysis data (from Step 2)
- Confirmed style + mood (from Step 3)
- Confirmed image counts (from Step 4)
- Active brand config loaded (from Step 1)

## Procedure

### For Each Requested Image

#### 1. Load Image Type Template

Read the prompt section template from `references/image-types/{type}.md`:
- `cover-hero.md` for cover hero images
- `facebook-card.md` for Facebook cards
- `instagram-card.md` for Instagram cards (single or carousel)

Copy the template as the starting point.

#### 2. Load Style Reference

Read `references/styles/{confirmed_style}.md` and extract from the "Prompt Fragments" section:
- `style_descriptor` -- inject into the STYLE line
- `visual_constraints` -- inject into the CONSTRAINTS section
- `negative_prompt` -- append to the NEGATIVE line

#### 3. Load Brand Palette

Read `config/brands/{active_brand}.json` and extract palette values:
- Replace all `{primary_hex}` with `palette.primary.hex`
- Replace all `{secondary_hex}` with `palette.secondary.hex`
- Replace all `{accent_hex}` with `palette.accent.hex`
- Replace all `{background_hex}` with `palette.background.light` (default) or `.dark` (if mood is dark)
- Replace all `{text_color}` with `palette.text.on_light` or `.on_dark`
- Replace font references with `typography.*` values

**If any value is `TO_BE_PROVIDED`**: replace with a descriptive role name:
- `TO_BE_PROVIDED` primary -> "brand primary color (dominant, trustworthy)"
- `TO_BE_PROVIDED` secondary -> "brand secondary color (supporting)"
- `TO_BE_PROVIDED` accent -> "brand accent color (highlights, emphasis)"

#### 4. Fill Article Context

Replace content placeholders with extracted article data:
- `{article_title}` -> article title from frontmatter
- `{primary_keyword}` -> primary keyword from frontmatter
- `{visual_theme}` -> inferred topic category
- `{topic_illustration_subject}` -> specific visual elements list

#### 5. Generate Social Card Content (facebook-card and instagram-card only)

This is where Claude generates NEW content, not copies from the article:

**For facebook-card:**
- `{summary_headline}` -> Distill core value into max 8 words. Must be punchier than article title.
- `{compelling_stat}` -> Select the single most impressive statistic from extracted stats.
- `{action_phrase}` -> Write a brief CTA (e.g., "Read the full guide", "See the checklist").

**For instagram-card (single):**
- `{summary_headline}` -> Article title or adapted 2-line version
- `{stat_1}`, `{stat_2}` -> Top 2 statistics

**For instagram-card (carousel):**
- Generate content for each slide:
  - Title slide: `{article_title}` + most visually interesting stat
  - Content slides: one per TL;DR point or key takeaway
  - CTA slide: "Read the full article" + brand identity

#### 6. Apply Mood Modifier

Append mood instructions after the main prompt:

- **professional**: "Muted, restrained color application. Subtle contrast. Clean lines. Convey authority, trust, and expertise. No playful elements."
- **energetic**: "Vibrant saturation. High contrast between elements. Dynamic composition with diagonal lines or asymmetric balance. Convey excitement, opportunity, and forward momentum."
- **warm**: "Softer color tones, gentle gradients where style permits. Rounded shapes emphasized. Inviting composition. Convey approachability, care, and human connection."

#### 7. Save Prompt File

Save to: `data/images/YYYYMMDD/{article-slug}/prompts/{type}-{N}-prompt.md`

Format:
```yaml
---
image_type: {type}
style: {style}
mood: {mood}
brand: {brand_id}
article_source: {article_path}
generated_at: {ISO timestamp}
backend: {backend from config}
---

{assembled prompt text}
```

Naming:
- Single image: `cover-hero-prompt.md`, `facebook-card-1-prompt.md`
- Multiple of same type: `facebook-card-1-prompt.md`, `facebook-card-2-prompt.md`
- Carousel: `instagram-card-carousel-prompt.md` (contains all slides in one file with slide separators)

## Carousel Prompt Format

For Instagram carousel, all slides go in one prompt file with separators:

```
--- SLIDE 1 OF {total}: TITLE ---
{title slide prompt}

--- SLIDE 2 OF {total}: CONTENT ---
{content slide prompt}

--- SLIDE 3 OF {total}: CONTENT ---
{content slide prompt}

--- SLIDE {total} OF {total}: CTA ---
{CTA slide prompt}
```

Each slide section follows the carousel template from `instagram-card.md`.
