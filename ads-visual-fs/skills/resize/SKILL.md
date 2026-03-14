---
name: resize
description: >
  Activates when the user wants to resize an ad, adapt for Instagram, create platform versions,
  make a Facebook ad, generate multi-platform sizes, adapt for social media, or says things like
  "resize this for Instagram", "make platform versions", "adapt this for social", "create
  LinkedIn and TikTok versions".
metadata:
  version: "0.2.0"
---

# Resize Ad for Platforms

Adapt an ad creative for different platform formats with composition-aware recomposition.

## Trigger

This skill auto-activates when the user provides an ad image and mentions platform names or resizing.

## Workflow

Follow the exact same workflow as the `/resize` command. Read the command at `../../commands/resize.md` for the full orchestration steps.

The key steps are:

1. **Analyze** — Read image, determine aspect ratio and composition. YOU analyze directly. **Document composition notes** — record element positions (e.g., "logo top-left, headline center-top, CTA bottom-center, product image right-third") and visual hierarchy. You will pass these notes to the script in Step 3.
2. **Select Platforms** — Parse from user message or present menu. Available: Instagram Feed (1:1), Instagram Story/Reel (9:16), Facebook Feed (4:3), Facebook Story (9:16), LinkedIn Feed (4:3), LinkedIn Story (9:16), TikTok (9:16), YouTube Thumbnail (16:9), Google Display Leaderboard (16:9), Google Display Rectangle (4:3), Google Display Skyscraper (9:16).
3. **Generate** — Run the generate-image.ts script via Bash for each platform, passing the composition notes from Step 1 in the `--prompt` and the target aspect ratio via `--ar`.
   ```bash
   ${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
     --prompt "Adapt for <platform>. <composition notes: element positions and hierarchy>" \
     --image "./ads-output/resize/<platform>.png" \
     --ref "<source image>" \
     --ar "<target aspect ratio>" \
     --json
   ```
4. **Review** — List all files with specs. Offer to regenerate or refine specific versions.

## Important

- YOU do all composition analysis. Image resizing is done via the `generate-image.ts` script executed through Bash.
- Process platforms sequentially to avoid rate limits.
- If the script fails, wait 5s, retry once, then continue with remaining platforms.
- See `../image-editing/references/platform-specs.md` for detailed dimensions, safe zones, and platform key mapping.
