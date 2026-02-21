# Base Prompt Assembly

## Prompt Architecture

The final image generation prompt is assembled from four layers, applied in order:

### Layer 1: Image Type Foundation
- Source: `references/image-types/{type}.md` -> "Prompt Section Template"
- Provides: dimensions, layout, composition rules, text element slots
- Sets the structural frame for the image

### Layer 2: Style Application
- Source: `references/styles/{style}.md` -> "Prompt Fragments"
- Provides: `style_descriptor`, `visual_constraints`, `negative_prompt`
- Injected into the composition and visual element sections

### Layer 3: Brand Palette
- Source: `config/brands/{active_brand}.json` -> `palette`
- Provides: specific hex colors mapped to primary/secondary/accent/background/text roles
- If palette has `TO_BE_PROVIDED` values, use descriptive role names instead (e.g., "brand primary color" instead of "#FF6B00")

### Layer 4: Article Context
- Source: article markdown file (from `data/drafts/YYYYMMDD/`)
- Extracted from YAML frontmatter:
  - `title`
  - `primary_keyword`
  - `content_pillar`
- Extracted from article body:
  - `key_statistics` -- first 3 RM values or percentages found
  - `tl_dr_points` -- bullet points from TL;DR section
  - `visual_theme` -- inferred topic category (finance, tax, technology, tourism, etc.)
  - `core_benefit` -- single sentence describing what reader gains

## Assembly Procedure

1. **Start with Image Type template** -- copy the prompt section template from the matching image-type reference file
2. **Insert Style descriptors** -- replace `{style_descriptor}`, `{visual_constraints}`, `{negative_prompt}` with values from the style reference file's Prompt Fragments section
3. **Apply Palette colors** -- replace all `{*_hex}` placeholders with actual hex values from the brand config. If values are `TO_BE_PROVIDED`, use role descriptions instead.
4. **Fill Article Context** -- replace `{article_title}`, `{primary_keyword}`, `{visual_theme}`, and all content-specific slots with extracted article data
5. **Apply Mood modifier** -- append mood instructions:
   - `professional`: Muted tones, subtle contrast, restrained composition. Convey authority and trust.
   - `energetic`: Vibrant saturation, high contrast, dynamic angles. Convey excitement and opportunity.
   - `warm`: Softer colors, rounded shapes emphasized, gentle gradients. Convey approachability and care.
6. **Append negative prompt** -- add the style's negative prompt as a final exclusion list

## Social Card Content Generation

For `facebook-card` and `instagram-card`, the text content is NOT copied from the article. Claude generates summary content during prompt assembly:

### Facebook Card Content
- **Headline**: Distill the article's core value into max 8 words. Must be punchier than the article title.
- **Key Stat**: Select the single most compelling statistic (highest RM value or most surprising percentage).
- **CTA Hint**: Write a brief action phrase (e.g., "Read the full guide", "See the 5-step checklist").

### Instagram Card Content (Single)
- **Headline**: Article title or adapted summary (max 2 lines)
- **Key Stats**: Top 1-2 data points from article

### Instagram Carousel Content
- **Title Slide**: Article title + most visually interesting stat as hook
- **Content Slides**: One per TL;DR bullet point (or top 3-5 takeaways if no TL;DR). Each needs: heading (5-8 words), supporting stat, visual metaphor.
- **CTA Slide**: "Read the full article" + brand identity

## Final Prompt Template

```
Create a {image_type_name} image.

DIMENSIONS: {width}x{height}px ({aspect_ratio})

STYLE: {style_descriptor}
{visual_constraints}

COLOR PALETTE:
- Primary: {primary_hex} ({primary_name})
- Secondary: {secondary_hex} ({secondary_name})
- Accent: {accent_hex} ({accent_name})
- Background: {background_hex}
- Text: {text_color}

COMPOSITION:
{composition_rules_from_image_type}

TEXT ELEMENTS:
{text_elements_from_image_type_with_article_values}

VISUAL THEME: {visual_theme} -- {topic_illustration_subject}

MOOD: {mood_descriptor}

CONSTRAINTS:
- No realistic human faces or photographs
- No text spelling errors (verify all text elements)
- {style_negative_prompt}
- Maintain {brand_name} visual identity: {brand_descriptors}
```

## Saved Prompt File Format

Each prompt is saved as a markdown file with YAML frontmatter for traceability:

```yaml
---
image_type: cover-hero
style: flat-vector
mood: professional
brand: funding-societies
article_source: data/drafts/20260208/article-slug.md
generated_at: 2026-02-08T14:30:00+08:00
backend: prompt-only
---

[Assembled prompt text here]
```
