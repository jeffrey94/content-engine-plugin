# Facebook Card Image

## Purpose

Summary visual for Facebook post promoting the article. This is a **standalone summary image** -- NOT a resized cover. It communicates the article's core value proposition at a glance in the Facebook feed, where users scroll quickly and decide in 1-2 seconds whether to engage.

## Dimensions

- **Aspect Ratio:** 1.91:1 (Facebook link preview standard)
- **Recommended Resolution:** 1200 x 628 px
- **Minimum Resolution:** 600 x 314 px
- **File Format:** PNG or WebP

## Composition Rules

- **Visual Weight:** 40-50% illustration, 50-60% text/info area
- **Layout:** Split composition -- visual element on one side, text summary on the other (left-right or top-bottom)
- **Text Zone:** Large, clear area for headline + 1-2 key stats. Must be readable at thumbnail size.
- **Brand Element:** Logo in corner per brand config `logo.placement_preference`
- **Information Hierarchy:** Headline (largest) > Key stat (medium) > CTA hint (smallest)
- **Visual Simplicity:** Facebook feed is noisy. Use fewer elements with stronger contrast than cover-hero.

## Text Elements (Content Summary)

These are **generated from article analysis**, not copied from the article title:

- **Headline:** Punchy summary of core value. Maximum 8 words. May differ from article title.
  - Example: Article title "Complete Guide to E-Invoicing Phase 2 for Malaysian SMEs" becomes headline "E-Invoicing Phase 2: What SMEs Must Know"
- **Key Stat:** The single most compelling RM value or percentage from the article.
  - Example: "RM50,000+ potential tax savings" or "87-day average payment delay"
- **CTA Hint:** Brief action phrase encouraging click-through.
  - Example: "Read the full guide" or "See the 5-step checklist"
- **Logo:** Included per brand config placement rules.

## Content Extraction

From the article analysis (Step 2), extract:
1. Scan article body for the **single most compelling statistic** (highest RM value or most surprising percentage)
2. Distill the **core reader benefit** into 8 words or fewer
3. Identify the **primary action** the reader should take after reading
4. These three elements form the headline, key stat, and CTA hint

## Style Interaction

| Style | Facebook Card Notes |
|---|---|
| flat-vector | Recommended. Clarity at small display sizes. |
| isometric | Caution: simplify significantly. Single small isometric element only. |
| hand-drawn | Good. Warm and approachable in feed. |
| corporate-modern | Recommended. Professional and clean. |
| bold-graphic | Recommended. High contrast catches attention in feed. |
| watercolor | Caution: readability concern. Use solid text backing. |
| minimal-line | Recommended. Clean at any size. |
| data-visual | Good. Single chart element as visual anchor. |
| cultural-motif | Good. Pattern border frames text effectively. |

## Prompt Section Template

```
IMAGE TYPE: Facebook link preview card
DIMENSIONS: 1200x628px (1.91:1)
LAYOUT: Split composition -- visual illustration element on {left_or_right}, text summary area on {opposite_side}. 40-50% visual, 50-60% text.
HEADLINE: "{summary_headline}" -- large, bold, {brand_heading_font}
KEY STAT: "{compelling_stat}" -- medium size, {brand_accent_hex} color for emphasis
CTA: "{action_phrase}" -- small, subtle, below headline
LOGO: {brand_name} logo at {logo_placement_preference}, respecting {min_clear_space}
COLOR PALETTE: Primary {primary_hex}, Secondary {secondary_hex}, Accent {accent_hex}, Background {background_hex}
STYLE: {style_descriptor}
MOOD: {mood_descriptor}
CONSTRAINTS: {visual_constraints}. Simplified composition (fewer elements than cover). Text readable at 300px width. No realistic human faces.
NEGATIVE: {negative_prompt}
```
