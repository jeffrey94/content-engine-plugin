# Instagram Card Image

## Purpose

Visual summary for Instagram post promoting the article. Can be a **single image** or a **carousel** (multi-slide). Summarizes the article's key points visually for a social media audience that is highly visual-first. Instagram users expect polished, well-designed content.

## Dimensions

### Single Image
- **Aspect Ratio:** 1:1 (square)
- **Resolution:** 1080 x 1080 px

### Carousel Slides
- **Aspect Ratio:** 4:5 (portrait, more screen real estate)
- **Resolution:** 1080 x 1350 px

### File Format
PNG or WebP

## Single Image Mode

### Composition Rules
- **Visual Weight:** 50% illustration, 50% text
- **Layout:** Centered or stacked (visual top, text bottom)
- **Text Zone:** Bottom third or center overlay
- **Brand Element:** Logo + thin color bar at bottom
- **Visual Impact:** Must work as a standalone piece -- no click-through context like Facebook

### Text Elements
- **Headline:** Article title or adapted summary (max 2 lines)
- **Key Stats:** 1-2 most compelling data points
- **Brand Bar:** Thin strip at bottom with brand primary color + logo

## Carousel Mode

### Structure
- **Slide 1 (Title):** Article title + hero visual + brand identity
- **Slides 2 to N (Content):** One key takeaway per slide, each with its own visual element
- **Final Slide (CTA):** "Read the full article" + URL hint + logo + brand bar

### Slide Composition Rules
- **Consistent Frame:** Same border width, color scheme, and font across ALL slides
- **One Idea Per Slide:** Single stat, single insight, single visual metaphor
- **Visual Continuity:** Same art style applied uniformly to all slides
- **Slide Counter:** Optional "1/N" indicator in top-right corner
- **Swipe Flow:** Each slide should feel like a natural continuation -- build a narrative arc

### Content Slide Layout
- **Top 40%:** Visual element illustrating the key point
- **Bottom 60%:** Heading (1 line) + supporting text (2-3 lines max)
- **Accent Element:** Brand accent color used for emphasis (underlines, highlight boxes)

### Content Extraction for Carousel
1. Parse article for **TL;DR section** -- each bullet becomes one carousel slide
2. If no TL;DR, extract **3-5 key takeaways** from article body
3. Each takeaway needs: a heading (5-8 words), a supporting stat or fact, a visual metaphor
4. Title slide uses the **most visually interesting stat** as a hook
5. CTA slide includes the article slug or a short URL hint

## Style Interaction

| Style | Instagram Notes |
|---|---|
| flat-vector | Recommended. Clean, scales perfectly for mobile. |
| isometric | Good. Single scene works well in square format. |
| hand-drawn | Recommended. Strong Instagram aesthetic appeal. |
| corporate-modern | Good. Professional but may feel less "native" to Instagram. |
| bold-graphic | Recommended. Eye-catching, high engagement potential. |
| watercolor | Good. Beautiful aesthetic for Instagram's visual audience. |
| minimal-line | Recommended. Elegant, distinctive in feed. |
| data-visual | Recommended for carousel. Each slide can feature one data point beautifully. |
| cultural-motif | Recommended. Culturally resonant, visually distinctive. Strong engagement. |

## Prompt Section Template (Single)

```
IMAGE TYPE: Instagram post (square)
DIMENSIONS: 1080x1080px (1:1)
LAYOUT: Stacked -- visual element in upper half, text summary in lower half. 50/50 split.
HEADLINE: "{summary_headline}" -- bold, {brand_heading_font}
KEY STATS: "{stat_1}", "{stat_2}" -- {brand_accent_hex} color emphasis
BRAND BAR: Thin {brand_primary_hex} strip at bottom with {brand_name} logo
COLOR PALETTE: Primary {primary_hex}, Secondary {secondary_hex}, Accent {accent_hex}, Background {background_hex}
STYLE: {style_descriptor}
MOOD: {mood_descriptor}
CONSTRAINTS: {visual_constraints}. Mobile-first design. Text readable without zooming. No realistic human faces.
NEGATIVE: {negative_prompt}
```

## Prompt Section Template (Carousel Slide)

```
IMAGE TYPE: Instagram carousel slide {N} of {total}
DIMENSIONS: 1080x1350px (4:5 portrait)
SLIDE TYPE: {title|content|cta}
SLIDE CONTENT: "{slide_heading}" -- "{slide_stat_or_insight}"
VISUAL: {style-specific illustration element} representing {point_visual_metaphor}
FRAME: Consistent {brand_primary_hex} border (4px), {brand_name} footer bar
TYPOGRAPHY: {brand_heading_font} for heading, {brand_body_font} for body text
COLOR PALETTE: Primary {primary_hex}, Secondary {secondary_hex}, Accent {accent_hex}, Background {background_hex}
STYLE: {style_descriptor}
MOOD: {mood_descriptor}
SLIDE COUNTER: "{N}/{total}" in top-right, {brand_muted_text} color, small
CONSTRAINTS: {visual_constraints}. One idea per slide. Visual continuity with other slides. Mobile-first. No realistic human faces.
NEGATIVE: {negative_prompt}
```
