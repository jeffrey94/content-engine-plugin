# Style Presets

Named shortcuts that set Style + Mood combinations for quick selection.

## Rules

- Explicit `--style` or `--mood` flags **always override** preset values
- Presets only set style + mood. **Color palette is always loaded from the active brand config** -- presets never set colors.
- Presets can be used in Step 3 confirmation: "Use preset standard" or via flag: `--preset standard`

## Preset Table

| Preset | Style | Mood | Best For |
|---|---|---|---|
| `standard` | corporate-modern | professional | Default for most blog posts. Safe, polished, authoritative. |
| `data-vis` | data-visual | professional | Statistics-heavy articles, financing content, survey reports. |
| `friendly` | hand-drawn | warm | Practical guides, how-to content, beginner-friendly articles. |
| `impact` | bold-graphic | energetic | Breaking policy news, urgent deadlines, important announcements. |
| `cultural` | cultural-motif | warm | Malaysian cultural topics, Visit Malaysia, local heritage. |
| `clean` | minimal-line | professional | Executive content, premium feel, strategy pieces. |
| `tech` | isometric | professional | Technology, infrastructure, supply chain, data center topics. |
| `creative` | watercolor | warm | Success stories, community content, lifestyle articles. |
| `flat` | flat-vector | professional | General-purpose, policy & compliance, clean infographic style. |

## Preset Selection by Content Pillar

| Content Pillar | Primary Preset | Alternative Preset |
|---|---|---|
| Policy & Compliance | `standard` | `flat` |
| Funding & Financing | `data-vis` | `standard` |
| Industry Opportunities | `tech` | `impact` |
| Practical Guides | `friendly` | `flat` |

## Custom Presets

Users can define custom presets in EXTEND.md:

```yaml
custom_presets:
  my-preset:
    style: watercolor
    mood: energetic
  compliance-urgent:
    style: bold-graphic
    mood: professional
```

Custom presets follow the same rules as built-in presets: explicit flags override, palette always from brand config.
