---
name: reimagine
description: >
  Activates when the user wants to reimagine an ad, create ad variations, remix a marketing visual,
  generate concept variations from an existing ad, transform an ad creative, or says things like
  "reimagine this ad", "create variations of this ad", "remix this creative", "give me 3 versions
  of this ad".
metadata:
  version: "0.2.0"
---

# Reimagine Ad Creative

Transform an existing ad creative into fresh concept variations at three conceptual levels: SAFE (Reframe), BOLD (Transform), and EXPERIMENTAL (Transcend).

## Trigger

This skill auto-activates when the user provides an ad image and wants variations. Look for the image path in their message.

## Workflow

Follow the exact same workflow as the `/reimagine` command. Read the command at `../../commands/reimagine.md` for the full orchestration steps.

The key steps are:

1. **Analyze** — Read the user's image. YOU analyze it directly (multimodal) for marketing insights: product, message, audience, brand codes, mandatory copy. Present and get user confirmation.
2. **Generate Concepts** — YOU generate 3 concept variations (SAFE/BOLD/EXPERIMENTAL) with titles, rationales, and image prompts. Get user selection.
3. **Generate Images** — Run the generate-image.ts script via Bash with the original as `--ref`. Set `--strength` per concept level: SAFE 0.55–0.65, BOLD 0.70–0.80, EXPERIMENTAL 0.85–0.95.
   ```bash
   ${BUN_X} ${CLAUDE_PLUGIN_ROOT}/scripts/generate-image.ts \
     --prompt "<concept prompt>" \
     --image "./ads-output/reimagine/<name>.png" \
     --ref "<original image>" \
     --strength <0.55-0.95> \
     --ar "<aspect ratio>" \
     --json
   ```
4. **Review** — Present outputs. Offer to refine or resize.

## Important

- YOU do all analysis and concept generation. Image generation is done via the `generate-image.ts` script executed through Bash.
- Always inject FS brand colors (#F1F1F2, #FFDE0F, #5203EA, #27E4CD, #2C50FF) and Poppins/Inter fonts into prompts.
- Always append the brand-compliance prompt injection template to all image generation prompts.
- Include user confirmation gates before proceeding to the next step.
- If Gemini fails, wait 5s and retry once.
