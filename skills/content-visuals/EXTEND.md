# Content Visuals - User Preferences

## Style Preferences
preferred_style: null
# Options: flat-vector, isometric, hand-drawn, corporate-modern, bold-graphic,
#          watercolor, minimal-line, data-visual, cultural-motif
# Set to null for auto-selection based on article content

preferred_mood: professional
# Options: professional, energetic, warm

default_preset: null
# Named preset from style-presets.md. Used when --quick flag is set.
# Options: standard, data-vis, friendly, impact, cultural,
#          clean, tech, creative, flat

## Image Defaults
default_cover_hero_count: 1
default_facebook_card_count: 1
default_instagram_card_count: 1
# Default quantities when user doesn't specify. 0 = skip that type.

instagram_mode: single
# Options: single | carousel
# When carousel: generates title + content slides + CTA slide

## Workflow Preferences
quick_mode: false
# true = skip confirmation steps, use auto-selection or preset
# false = ask for confirmation at each checkpoint

always_generate_prompts: true
# Always save prompt .md files regardless of backend

show_auto_selection_reasoning: true
# When auto-selecting style, show the reasoning to user

## Brand Override
brand_override: null
# Set to a brand_id to override config/brands/_active.json
# Useful for generating images for multiple brands in one session

## Output Preferences
include_manifest: true
# Save manifest.json with run metadata

prompt_language: en
# Language for prompt text: en, ms (Malay), zh

## Custom Presets
custom_presets: null
# Define custom preset combinations:
# custom_presets:
#   my-preset:
#     style: watercolor
#     mood: energetic
#   compliance-urgent:
#     style: bold-graphic
#     mood: professional
