---
name: image-editing
description: >
  Activates when transforming, refining, or resizing an existing image using a reference.
  Guides script usage for image-to-image generation, element refinement, and platform
  resizing. This is a shared capability, not a user-facing workflow.
metadata:
  version: "0.2.0"
---

# Image Editing (Image-to-Image)

Transform, refine, or resize existing ad images. Used by Reimagine, Refine, and Resize workflows.

## When This Activates

This skill provides guidance when you need to run the `generate-image.ts` script WITH a reference image:
- Reimagine: `--ref` with `--strength` (image-to-image with concept)
- Refine: `--ref` with change/preserve instructions in `--prompt`
- Resize: `--ref` with `--ar` for target platform

## Bash Script Usage

### For Reimagine (image-to-image with concept)

```bash
${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
  --prompt "<concept prompt>" \
  --image "./ads-output/reimagine/<name>.png" \
  --ref "<original image>" \
  --strength <0.55-0.95 based on concept level> \
  --ar "<aspect ratio>" \
  --json
```

### For Refine (targeted element changes)

```bash
${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
  --prompt "Refine: <specific changes>. Preserve: <logo, background, ...>" \
  --image "./ads-output/refine/<name>.png" \
  --ref "<source image>" \
  --json
```

### For Resize (platform adaptation)

```bash
${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
  --prompt "Adapt for <platform>. <element positions and hierarchy>" \
  --image "./ads-output/resize/<platform>.png" \
  --ref "<source image>" \
  --ar "<target aspect ratio>" \
  --json
```

## Image Strength Guide

| Strength | Effect | Use When |
|----------|--------|----------|
| 0.55–0.65 | Close to original | SAFE concepts, minor variations |
| 0.70–0.80 | Moderate transformation | BOLD concepts, new composition |
| 0.85–0.95 | Major transformation | EXPERIMENTAL concepts, genre shifts |

## Error Handling

1. If the script returns rate limit (429) or service unavailable (503): wait 5 seconds, retry once
2. If content policy violation: present the error, offer to modify the prompt
3. If no image data returned: retry with simplified prompt
