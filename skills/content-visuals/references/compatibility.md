# Compatibility Matrices

## Style x Image Type

Shows how well each art style works with each image output type.

| Style | cover-hero | facebook-card | instagram-card |
|---|---|---|---|
| flat-vector | Recommended | Recommended | Recommended |
| isometric | Recommended | Caution | Good |
| hand-drawn | Good | Good | Recommended |
| corporate-modern | Recommended | Recommended | Good |
| bold-graphic | Recommended | Recommended | Recommended |
| watercolor | Good | Caution | Good |
| minimal-line | Recommended | Recommended | Recommended |
| data-visual | Recommended | Good | Recommended |
| cultural-motif | Good | Good | Recommended |

### Caution Notes

- **isometric + facebook-card**: Isometric scenes have too much detail for small Facebook preview sizes (600px wide). If this combo is chosen, simplify to a single small isometric object rather than a full scene.
- **watercolor + facebook-card**: Watercolor's soft edges can make text hard to read at thumbnail sizes. Must use a solid-color text backing panel (not transparent overlay).

## Style x Mood

Shows which mood settings work best with each art style.

| Style | professional | energetic | warm |
|---|---|---|---|
| flat-vector | Recommended | Good | Good |
| isometric | Recommended | Recommended | Avoid |
| hand-drawn | Good | Good | Recommended |
| corporate-modern | Recommended | Good | Avoid |
| bold-graphic | Good | Recommended | Avoid |
| watercolor | Avoid | Avoid | Recommended |
| minimal-line | Recommended | Avoid | Good |
| data-visual | Recommended | Good | Avoid |
| cultural-motif | Good | Avoid | Recommended |

### Avoid Notes

- **isometric + warm**: Isometric's technical precision clashes with warm's soft, organic feel.
- **corporate-modern + warm**: Corporate polish contradicts warm approachability.
- **bold-graphic + warm**: Bold's high contrast and drama conflicts with warm's gentle tone.
- **watercolor + professional**: Watercolor's organic imprecision undermines professional authority.
- **watercolor + energetic**: Watercolor is inherently calm and flowing; energetic vibrance clashes.
- **minimal-line + energetic**: Minimal's restraint contradicts energetic's vibrancy.
- **data-visual + warm**: Data aesthetics feel clinical, not warm.
- **cultural-motif + energetic**: Cultural patterns are best with calm, respectful presentation.

## Style x Brand Palette Interaction

General rules for how styles use brand colors:

| Style | Primary Color Usage | Secondary Color Usage | Accent Color Usage |
|---|---|---|---|
| flat-vector | Dominant fills (40-50%) | Supporting fills (30%) | Small highlights (10%) |
| isometric | Surface colors on faces | Shadow tones | Edge highlights |
| hand-drawn | Sketch line color | Fill washes | Annotation highlights |
| corporate-modern | Headers, key elements | Backgrounds, panels | CTAs, links |
| bold-graphic | Large shape fills (50%+) | Contrast backgrounds | Minimal, impact only |
| watercolor | Primary wash color | Background wash | Splatter accents |
| minimal-line | Line color | Not used (whitespace) | Single accent element |
| data-visual | Chart element fills | Grid/axis lines | Data highlights |
| cultural-motif | Pattern primary color | Pattern secondary fill | Detail accents |

## Usage in Workflow

In Step 3 (Style Recommendation):
1. After auto-selecting a style + mood, check this matrix
2. If the combination is "Avoid", switch to the secondary style from auto-selection
3. If the combo is "Caution" for a requested image type, warn the user with the caution note
4. Always present compatibility status in the recommendation summary
