# EXTEND.md Preferences Schema

## Purpose

Documents all fields available in the `EXTEND.md` user preferences file for the content-visuals skill.

## File Location

`.claude/skills/content-visuals/EXTEND.md` (relative to project root)

## Field Reference

### Style Preferences

| Field | Type | Default | Options | Description |
|---|---|---|---|---|
| `preferred_style` | string or null | `null` | flat-vector, isometric, hand-drawn, corporate-modern, bold-graphic, watercolor, minimal-line, data-visual, cultural-motif | Default art style. `null` = auto-select based on article content. |
| `preferred_mood` | string | `professional` | professional, energetic, warm | Default mood when not auto-selected. |
| `default_preset` | string or null | `null` | Any preset name from style-presets.md | Preset used when `--quick` flag is set. |

### Image Defaults

| Field | Type | Default | Range | Description |
|---|---|---|---|---|
| `default_cover_hero_count` | integer | `1` | 0-3 | Default cover hero images per run. 0 = skip. |
| `default_facebook_card_count` | integer | `1` | 0-5 | Default Facebook card images per run. 0 = skip. |
| `default_instagram_card_count` | integer | `1` | 0-10 | Default Instagram card images per run. 0 = skip. |
| `instagram_mode` | string | `single` | single, carousel | Single image or multi-slide carousel. |

### Workflow Preferences

| Field | Type | Default | Description |
|---|---|---|---|
| `quick_mode` | boolean | `false` | Skip confirmation steps, use auto-selection or default preset. |
| `always_generate_prompts` | boolean | `true` | Always save prompt .md files regardless of backend. |
| `show_auto_selection_reasoning` | boolean | `true` | Display reasoning when auto-selecting style. |

### Brand Override

| Field | Type | Default | Description |
|---|---|---|---|
| `brand_override` | string or null | `null` | Brand ID to override `config/brands/_active.json`. Useful for multi-brand sessions. |

### Output Preferences

| Field | Type | Default | Options | Description |
|---|---|---|---|---|
| `include_manifest` | boolean | `true` | | Save manifest.json with run metadata. |
| `prompt_language` | string | `en` | en, ms, zh | Language for prompt text content. |

### Custom Presets

| Field | Type | Default | Description |
|---|---|---|---|
| `custom_presets` | object or null | `null` | User-defined preset combinations. Each key is a preset name, value has `style` and `mood` fields. |

## Example EXTEND.md

```yaml
# Content Visuals - User Preferences

preferred_style: null
preferred_mood: professional
default_preset: standard

default_cover_hero_count: 1
default_facebook_card_count: 1
default_instagram_card_count: 1
instagram_mode: single

quick_mode: false
always_generate_prompts: true
show_auto_selection_reasoning: true

brand_override: null

include_manifest: true
prompt_language: en

custom_presets: null
```
