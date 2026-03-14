---
name: resize
description: Adapt an ad for different platform formats
argument-hint: <image-path> [platforms]
allowed-tools: Read, Bash
---

# /resize

Adapt an ad creative for different platform formats with composition-aware recomposition.

## Step 1 — Analyze Source

Read the image at `$1`. Analyze it directly — you are multimodal.

Determine:
- Source aspect ratio (from image dimensions)
- Key elements and their positions (headline, CTA, logo, product, background)
- Visual hierarchy and composition notes

**Document composition notes** — record element positions (e.g., "logo top-left, headline center-top, CTA bottom-center") for use in Step 3.

## Step 2 — Select Platforms

If `$2` is provided, parse platform names from it (e.g., "instagram linkedin tiktok").

Otherwise, present the platform menu and ask the user to select:

**Social Media:**
- [ ] Instagram Feed (1:1)
- [ ] Instagram Story/Reel (9:16)
- [ ] Facebook Feed (4:3)
- [ ] Facebook Story (9:16)
- [ ] LinkedIn Feed (4:3)
- [ ] LinkedIn Story (9:16)
- [ ] TikTok (9:16)

**Display & Video:**
- [ ] YouTube Thumbnail (16:9)
- [ ] Google Display Leaderboard (16:9)
- [ ] Google Display Rectangle (4:3)
- [ ] Google Display Skyscraper (9:16)

> **Select platforms (comma-separated numbers or names):**

Wait for selection.

## Platform Specs

| Key | Aspect Ratio | Description |
|-----|-------------|-------------|
| instagram-feed | 1:1 | Instagram Feed (1080x1080) |
| instagram-story | 9:16 | Instagram Story (1080x1920) |
| facebook-feed | 4:3 | Facebook Feed (1200x900) |
| facebook-story | 9:16 | Facebook Story (1080x1920) |
| linkedin-feed | 4:3 | LinkedIn Feed (1200x627) |
| linkedin-story | 9:16 | LinkedIn Story (1080x1920) |
| tiktok | 9:16 | TikTok (1080x1920) |
| youtube-thumbnail | 16:9 | YouTube Thumbnail (1280x720) |
| google-leaderboard | 16:9 | Leaderboard (728x90) |
| google-rectangle | 4:3 | Medium Rectangle (300x250) |
| google-skyscraper | 9:16 | Wide Skyscraper (160x600) |

## Step 3 — Generate Resized Versions

For each selected platform, run the script via Bash with composition context:

```bash
${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
  --prompt "Adapt this marketing ad for <platform description>. Maintain all brand elements, copy, and visual hierarchy. Recompose the layout to fit the <ratio> aspect ratio naturally — do not simply crop or stretch. Ensure all text remains legible and the CTA is prominent. Composition: <composition notes from Step 1>" \
  --image "./ads-output/resize/<platform-key>.png" \
  --ref "$1" \
  --ar "<aspect ratio>" \
  --json
```

Process platforms sequentially to avoid rate limits.

**Runtime resolution**: If `bun` is installed, use `bun`. Otherwise use `npx -y bun`.

**Error handling**: If a script call fails, wait 5 seconds and retry once. If it still fails, log the error and continue with remaining platforms.

## Step 4 — Review

List all generated files with their platform specs:

| Platform | Dimensions | Aspect Ratio | Output Path |
|----------|-----------|--------------|-------------|
| ... | ... | ... | ... |

Offer:
- **Regenerate** — Retry specific platforms
- **Refine** — Make targeted changes to a specific platform version (→ suggest `/refine`)
