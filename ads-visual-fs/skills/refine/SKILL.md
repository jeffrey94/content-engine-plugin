---
name: refine
description: >
  Activates when the user wants to refine an ad, edit ad elements, change a headline, adjust a CTA,
  modify ad colors, tweak an ad creative, update copy, or says things like "change the headline",
  "make the CTA more urgent", "adjust the colors", "edit this ad", "tweak this creative".
metadata:
  version: "0.2.0"
---

# Refine Ad Elements

Make targeted changes to specific elements of an existing ad creative while preserving everything else.

## Trigger

This skill auto-activates when the user provides an ad image and describes specific changes. Look for the image path and change description in their message.

## Workflow

Follow the exact same workflow as the `/refine` command. Read the command at `../../commands/refine.md` for the full orchestration steps.

The key steps are:

1. **Collect Intent** — Read image, get change description from user or their message.
2. **Analyze Composition** — YOU analyze the image directly for element mapping (headline, CTA, logo, background, etc. with positions). Present the element map.
3. **Propose Changes** — Map intent to elements, present proposed changes table, show editable prompt and preserve list. Get confirmation.
4. **Generate** — Run the generate-image.ts script via Bash three times (v1, v2, v3) with slight prompt variations to produce diverse results. Use different phrasing or emphasis for each variation while keeping the core intent the same. Include the change instructions and preserve list in the `--prompt`. Save to `./ads-output/refine/<description>-v1.png`, `-v2.png`, `-v3.png`.
   ```bash
   ${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
     --prompt "Refine: <specific changes>. Preserve: <logo, background, ...>" \
     --image "./ads-output/refine/<description>-v1.png" \
     --ref "<source image>" \
     --json
   ```
5. **Review** — Present all 3 output paths. Offer further refine or resize.

## Important

- YOU do all composition analysis. Image editing is done via the `generate-image.ts` script executed through Bash.
- Always validate against FS brand guidelines before generating.
- User confirmation required before generating.
- If the script fails, wait 5s and retry once.
- Always append the brand-compliance prompt injection template to all image generation prompts.
