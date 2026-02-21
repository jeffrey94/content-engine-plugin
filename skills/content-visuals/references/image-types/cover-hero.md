# Cover Hero Image

## Purpose

Blog header image displayed at the top of the article on the website. Sets the visual tone for the entire piece and is the first thing readers see.

## Dimensions

- **Aspect Ratio:** 16:9 (landscape)
- **Recommended Resolution:** 1200 x 675 px
- **Minimum Resolution:** 800 x 450 px
- **File Format:** PNG (for quality) or WebP (for performance)

## Composition Rules

- **Visual Weight:** 60-70% illustration/graphic, 30-40% whitespace or text zone
- **Text Zone:** Upper-left or center overlay area for article title
- **Safe Zone:** Keep critical elements 10% inward from all edges (accounts for responsive cropping on mobile)
- **Visual Anchor:** Single focal illustration element, positioned using rule-of-thirds
- **Balance:** Avoid placing all visual weight on one side -- maintain left-right equilibrium
- **Negative Space:** Ensure enough breathing room around the focal element for the image to feel composed, not cramped

## Text Elements

- **Title:** Article title pulled from YAML frontmatter. Maximum 2 lines at display size.
- **Subtitle:** Optional. Use `primary_keyword` or `meta_description` from frontmatter. Maximum 1 line.
- **Logo:** NOT included on cover heroes (per brand config -- logo is reserved for social cards)
- **Text Contrast:** Text must have sufficient contrast against background. If background is busy, use a semi-transparent backing panel behind text.

## Content Extraction

From the article, extract:
1. `title` from YAML frontmatter
2. `primary_keyword` for optional subtitle
3. `content_pillar` for visual theme guidance
4. Main topic category to inform illustration subject (e.g., tax = calculator/forms, financing = money flow, technology = circuits/devices)

## Style Interaction

| Style | Cover Hero Notes |
|---|---|
| flat-vector | Recommended. Clean compositions scale well. |
| isometric | Recommended. Use a single isometric scene as focal point. |
| hand-drawn | Good. Sketch elements with generous whitespace. |
| corporate-modern | Recommended. Default choice for most articles. |
| bold-graphic | Recommended. Large shapes fill the frame well at this size. |
| watercolor | Good, but requires solid text backing panel for title readability. |
| minimal-line | Recommended. Whitespace-heavy, elegant. |
| data-visual | Recommended. Decorative chart elements as visual anchor. |
| cultural-motif | Good. Pattern elements frame the text zone effectively. |

## Prompt Section Template

```
IMAGE TYPE: Blog cover hero image
DIMENSIONS: 1200x675px (16:9 landscape)
COMPOSITION: Single focal illustration element positioned using rule-of-thirds. 60-70% visual, 30-40% text zone. 10% safe margin from edges.
TEXT OVERLAY: Title "{article_title}" in {brand_heading_font}, {brand_text_on_light_or_dark} color. Optional subtitle: "{primary_keyword}".
TEXT PLACEMENT: {text_zone_position} with semi-transparent backing if needed for contrast.
VISUAL THEME: {visual_theme} -- {topic_illustration_subject}
COLOR PALETTE: Primary {primary_hex}, Secondary {secondary_hex}, Accent {accent_hex}, Background {background_hex}
STYLE: {style_descriptor}
MOOD: {mood_descriptor}
CONSTRAINTS: {visual_constraints}. No logo. No realistic human faces. Generous whitespace. Text must be legible at 50% display size.
NEGATIVE: {negative_prompt}
```
