# Gemini Image Generation Backend

Implementation reference for generating images via the Google Gemini API using bash `curl`. For Claude Code users only.

## Prerequisites

### Environment Variable

The user must have `GEMINI_API_KEY` set in their shell environment or project `.env` file.

Check availability:
```bash
if [ -z "$GEMINI_API_KEY" ]; then
  echo "GEMINI_API_KEY not set"
  exit 1
fi
```

### Required Tools

Verify before first use:
```bash
for cmd in curl jq base64; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "$cmd is required but not installed"; exit 1; }
done
```

### Platform Detection

macOS and Linux use different `base64` decode flags:
```bash
OS="$(uname -s)"
if [ "$OS" = "Darwin" ]; then
  BASE64_DECODE_FLAG="-D"
else
  BASE64_DECODE_FLAG="-d"
fi
```

## Models

| Tier | Model ID | Best For | Notes |
|------|----------|----------|-------|
| `flash` | `gemini-2.5-flash-image` | Fast drafts, batch generation | Lower latency, good quality |
| `pro` | `gemini-3-pro-image-preview` | Final assets, high quality | 4K support, advanced reasoning, preview |

Default: `flash` (fast, production-ready). Use `pro` when quality matters more than speed.

## API Endpoint

```
https://generativelanguage.googleapis.com/v1beta/models/{MODEL_ID}:generateContent
```

## Request Format

### JSON Payload

Write to a temp file — never construct inline with shell interpolation (prompt text may contain quotes, newlines, special characters):

```bash
PAYLOAD_FILE="$(mktemp)"
cat > "$PAYLOAD_FILE" << 'PAYLOAD_END'
{
  "contents": [
    {
      "parts": [
        {
          "text": "PROMPT_PLACEHOLDER"
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": ["IMAGE", "TEXT"],
    "imageMimeType": "image/png"
  }
}
PAYLOAD_END
```

Then inject the actual prompt using `jq` (safe for special characters):

```bash
PROMPT_TEXT="$(cat "$PROMPT_FILE")"
jq --arg prompt "$PROMPT_TEXT" '.contents[0].parts[0].text = $prompt' "$PAYLOAD_FILE" > "${PAYLOAD_FILE}.tmp" && mv "${PAYLOAD_FILE}.tmp" "$PAYLOAD_FILE"
```

### API Call

```bash
RESPONSE_FILE="$(mktemp)"
MODEL_ID="gemini-2.5-flash-image"  # or gemini-3-pro-image-preview

curl -s -o "$RESPONSE_FILE" -w "%{http_code}" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d @"$PAYLOAD_FILE" \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent"
```

## Response Handling

### Extract Image Data

The response contains base64-encoded image data in `candidates[0].content.parts[]`. The image part has `inlineData` with `mimeType` and `data` fields:

```bash
# Check for API errors
if jq -e '.error' "$RESPONSE_FILE" > /dev/null 2>&1; then
  ERROR_MSG=$(jq -r '.error.message' "$RESPONSE_FILE")
  echo "API error: $ERROR_MSG"
  rm -f "$PAYLOAD_FILE" "$RESPONSE_FILE"
  exit 1
fi

# Extract base64 image data from the first image part
IMAGE_DATA=$(jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' "$RESPONSE_FILE" | head -1)

if [ -z "$IMAGE_DATA" ] || [ "$IMAGE_DATA" = "null" ]; then
  echo "No image data in response"
  rm -f "$PAYLOAD_FILE" "$RESPONSE_FILE"
  exit 1
fi
```

### Decode and Save

**CRITICAL: NEVER pipe raw base64 data to stdout.** It will flood the terminal with megabytes of encoded text. Always decode directly to a file:

```bash
echo "$IMAGE_DATA" | base64 $BASE64_DECODE_FLAG > "$OUTPUT_PATH"
```

### Validate Output

```bash
FILE_SIZE=$(wc -c < "$OUTPUT_PATH")
if [ "$FILE_SIZE" -lt 1000 ]; then
  echo "Warning: output file suspiciously small (${FILE_SIZE} bytes)"
  rm -f "$OUTPUT_PATH"
  exit 1
fi

# Verify it's actually a PNG
FILE_TYPE=$(file -b "$OUTPUT_PATH")
if echo "$FILE_TYPE" | grep -qi "png\|image"; then
  echo "Saved: $OUTPUT_PATH (${FILE_SIZE} bytes)"
else
  echo "Warning: output may not be a valid image (detected: ${FILE_TYPE})"
fi
```

## Cleanup

Always remove temp files:
```bash
rm -f "$PAYLOAD_FILE" "$RESPONSE_FILE"
```

## Safety Rules

1. **NEVER** pipe base64 data to stdout or echo it to the terminal
2. **NEVER** embed API keys directly in commands — always use `$GEMINI_API_KEY`
3. **ALWAYS** write payloads to temp files — shell interpolation breaks on complex prompts
4. **ALWAYS** use `jq` for JSON construction and parsing — never string concatenation
5. **ALWAYS** validate output file size with `wc -c` before reporting success
6. **ALWAYS** clean up temp files, even on error paths

## Error Handling

| Error | Cause | Action |
|-------|-------|--------|
| HTTP 400 | Bad request / invalid prompt | Check prompt formatting, retry with simplified prompt |
| HTTP 401/403 | Invalid or missing API key | Prompt user to check `GEMINI_API_KEY` |
| HTTP 429 | Rate limited | Wait and retry (flash: 10 RPM free tier) |
| HTTP 500 | Server error | Retry once, then fall back to prompt-only |
| Empty `IMAGE_DATA` | Safety filter or model refusal | Log the prompt, fall back to prompt-only, notify user |
| Small file (<1KB) | Corrupted decode | Delete file, retry once |

## Fallback Behavior

If generation fails for any image after one retry:
1. Log the error to the manifest
2. Confirm the prompt file is saved
3. Notify the user that the prompt is available for manual generation
4. Continue with remaining images (don't abort the whole batch)

## Complete Single-Image Example

```bash
#!/bin/bash
set -euo pipefail

# --- Config ---
PROMPT_FILE="$1"
OUTPUT_PATH="$2"
MODEL_ID="${3:-gemini-2.5-flash-image}"

# --- Checks ---
[ -z "$GEMINI_API_KEY" ] && { echo "Error: GEMINI_API_KEY not set"; exit 1; }
[ -f "$PROMPT_FILE" ] || { echo "Error: prompt file not found: $PROMPT_FILE"; exit 1; }
for cmd in curl jq base64; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "Error: $cmd required"; exit 1; }
done

# --- Platform ---
OS="$(uname -s)"
[ "$OS" = "Darwin" ] && B64="-D" || B64="-d"

# --- Build payload ---
PAYLOAD="$(mktemp)"
RESPONSE="$(mktemp)"
trap 'rm -f "$PAYLOAD" "$RESPONSE"' EXIT

PROMPT_TEXT="$(cat "$PROMPT_FILE")"
jq -n --arg prompt "$PROMPT_TEXT" '{
  contents: [{parts: [{text: $prompt}]}],
  generationConfig: {responseModalities: ["IMAGE","TEXT"], imageMimeType: "image/png"}
}' > "$PAYLOAD"

# --- Call API ---
HTTP_CODE=$(curl -s -o "$RESPONSE" -w "%{http_code}" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${GEMINI_API_KEY}" \
  -d @"$PAYLOAD" \
  "https://generativelanguage.googleapis.com/v1beta/models/${MODEL_ID}:generateContent")

if [ "$HTTP_CODE" != "200" ]; then
  echo "API returned HTTP $HTTP_CODE"
  jq -r '.error.message // "Unknown error"' "$RESPONSE" 2>/dev/null
  exit 1
fi

# --- Extract and decode ---
IMAGE_DATA=$(jq -r '.candidates[0].content.parts[] | select(.inlineData) | .inlineData.data' "$RESPONSE" | head -1)
[ -z "$IMAGE_DATA" ] || [ "$IMAGE_DATA" = "null" ] && { echo "No image in response"; exit 1; }

mkdir -p "$(dirname "$OUTPUT_PATH")"
echo "$IMAGE_DATA" | base64 $B64 > "$OUTPUT_PATH"

# --- Validate ---
FILE_SIZE=$(wc -c < "$OUTPUT_PATH" | tr -d ' ')
[ "$FILE_SIZE" -lt 1000 ] && { echo "Output too small (${FILE_SIZE}B)"; rm -f "$OUTPUT_PATH"; exit 1; }

echo "OK: $OUTPUT_PATH (${FILE_SIZE} bytes)"
```
