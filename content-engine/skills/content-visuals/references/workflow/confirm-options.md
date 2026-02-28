# Confirmation Checkpoint Format

## Purpose

Defines the format for user confirmation steps in the workflow. There are two blocking confirmation points: Step 3 (Style) and Step 4 (Image Count).

## Step 3: Style Recommendation Confirmation

### Display Format

Present the recommendation clearly with reasoning:

```
STYLE RECOMMENDATION
====================

Article: {article_title}
Content Pillar: {content_pillar}
Key Signals: {top_3_keywords_detected}

Recommended Style: {style_name}
Recommended Mood:  {mood_name}
Matching Preset:   {preset_name} (if any match)
Reason: {1-sentence explanation of why this combo fits}

Compatibility Check:
  - cover-hero:     {OK / Caution: reason}
  - facebook-card:  {OK / Caution: reason}
  - instagram-card: {OK / Caution: reason}

Alternative: {secondary_style} + {secondary_mood} ({why this could also work})

OPTIONS:
1. Accept recommendation ({style} + {mood})
2. Use alternative ({secondary_style} + {secondary_mood})
3. Use preset: [standard | data-vis | friendly | impact | cultural | clean | tech | creative | flat]
4. Custom: specify --style {name} --mood {name}
```

### Handling User Response

| Response | Action |
|---|---|
| Accept / "1" / "yes" / "ok" | Use recommended style + mood |
| Alternative / "2" | Use secondary style + mood |
| Preset name / "3" + name | Load preset from style-presets.md |
| Custom / "4" + flags | Parse style and mood, validate against compatibility matrix |
| No response / timeout | Use recommended (default) |

### Validation After Selection

After user confirms:
1. Check compatibility matrix for the final style + mood combination
2. If "Avoid" combination: warn user and suggest alternative. Do NOT block -- respect user's choice.
3. Check style x image-type compatibility for all planned image types
4. If "Caution": note the adjustment that will be made (e.g., "isometric will be simplified for facebook-card")

## Step 4: Image Count Confirmation

### Display Format

```
IMAGE COUNT
===========

How many of each image type would you like?

  Cover hero:      [suggested: 1]
  Facebook card:   [suggested: 1]
  Instagram card:  [suggested: 1]

  Instagram mode:  [single / carousel]
  (If carousel: how many content slides? Suggested: {tl_dr_count} based on article takeaways)

Enter counts or press Enter for suggested defaults.
Examples: "1, 2, 3" or "cover:1 fb:2 ig:carousel:4"
```

### Handling User Response

| Response | Action |
|---|---|
| Enter / blank | Use suggested defaults |
| Numbers (e.g., "1, 1, 3") | Map to cover, facebook, instagram counts in order |
| Named (e.g., "cover:1 fb:2 ig:carousel:5") | Parse named values |
| "skip facebook" / "no fb" / "0" for a type | Set that type count to 0 |
| "carousel" or "carousel:N" | Set instagram to carousel mode with N content slides |

### Validation

- At least 1 image must be requested total
- Instagram carousel: minimum 2 slides (title + 1 content), maximum 10 slides
- If all counts are 0: warn user and re-ask
