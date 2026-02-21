# Universal Visual Element Rules

## Purpose

Baseline rules that apply to ALL generated images regardless of style, mood, or image type. These are appended to every prompt as universal constraints.

## Mandatory Rules

### No Realistic Human Faces
- Never use photographic or realistic human faces
- Acceptable alternatives: simplified silhouettes, faceless figures, abstract people shapes, icon-style characters
- Reason: avoids uncanny valley, legal issues with likeness, and keeps focus on content

### No Photographs
- All visuals must be illustrated, not photographic
- No stock photo aesthetics, no photorealistic rendering
- The entire image should feel crafted and intentional

### Text Accuracy
- All text rendered in the image must be verified for spelling
- RM values and statistics must exactly match the source article
- If text rendering is unreliable in the generation backend, prefer fewer text elements with larger size

### Whitespace
- Minimum 30% whitespace (empty/background space) in every image
- Whitespace is a design element, not wasted space
- Prevents visual clutter and improves readability

### Readability
- All text must be legible at 50% of the intended display size
- For mobile: text must be readable on a 375px-wide screen
- Minimum effective font size equivalent: 14px at display size
- High contrast between text and background (WCAG AA minimum)

## Malaysian Context Elements

### Approved Visual Elements
When the article topic involves Malaysian context, these elements can be used:
- **Currency:** RM symbol, Malaysian banknotes (stylized, not realistic)
- **Landmarks:** Petronas Towers silhouette, parliament building, mosques (simplified)
- **Nature:** Tropical flora (hibiscus, palm fronds, rainforest canopy)
- **Culture:** Batik patterns, songket motifs, wau kite shapes, kongsi architecture
- **Government:** Simplified coat of arms elements, agency logos (stylized)
- **Business:** Shophouses, kedai, pasar malam stalls (simplified)

### Cultural Sensitivity Guidelines
- **Respectful representation:** No caricatures, no stereotypes
- **Multi-ethnic awareness:** Malaysia is Malay, Chinese, Indian, and East Malaysian. Avoid representing only one group.
- **Religious sensitivity:** No specific religious symbols unless the article is specifically about that topic. Mosques can appear as architectural elements.
- **Language:** Use Bahasa Malaysia and English appropriately. Avoid other languages unless article-specific.
- **Food:** Can reference Malaysian food culture (nasi lemak, roti canai, etc.) as visual elements when relevant

## Brand Consistency

### Logo Usage
- Follow brand config `logo.usage_on_images` rules
- Default: logo on social cards (facebook-card, instagram-card), NOT on cover-hero
- Maintain minimum clear space per brand config
- Never distort, recolor, or partially crop the logo

### Color Discipline
- Use brand palette colors as specified in the brand config
- Do not introduce colors outside the brand palette unless the style specifically requires it (e.g., cultural-motif may need traditional pattern colors)
- When extending beyond palette: use muted/desaturated versions that complement brand colors

### Typography Consistency
- Use brand-specified font categories from brand config
- Maintain consistent heading/body hierarchy across all images in a set
- For carousel slides: identical font choices across ALL slides

## Element Complexity by Image Type

| Image Type | Max Elements | Visual Complexity |
|---|---|---|
| cover-hero | 3-5 key elements | Medium -- one focal point with supporting elements |
| facebook-card | 2-3 key elements | Low -- must read at thumbnail size |
| instagram-card (single) | 3-4 key elements | Medium -- one focal point |
| instagram-card (carousel) | 1-2 per slide | Low per slide -- cumulative complexity across slides |
