---
name: content-quality-checklist
description: >
  Validate blog articles against a structured quality checklist. Use when the
  user asks to "review an article", "check quality", "validate content",
  "run quality checklist", "score this article", or needs to verify an article
  meets publishing standards before going live.
version: 0.2.0
---

# Content Quality Checklist

Dual-tier validation framework for blog articles. Choose the tier based on content type, then score against the checklist.

## Tier Selection

**Tier 1 — Government Content** (15-point checklist, pass: 13/15 = 86.7%)
Use for: Policy, compliance, government schemes, government financing programs.

**Tier 2 — Market Content** (12-point checklist, pass: 10/12 = 83.3%)
Use for: Market trends, success stories, operational guides, platform comparisons.

Load quality thresholds from `config/project.json` → `content.quality_thresholds`.

## Tier 1: Government Content (15 Points)

### 1. Hook with Specific Data
Check the first 2 paragraphs for a local currency value, percentage, or data point from a credible source.
- ❌ "Cash flow is important for SMEs"
- ✅ "[Audience] wait an average of X days for payment, tying up [currency][amount] in working capital [source]"

### 2. Statistics (3+ Required)
Search for local currency values, percentages, and numerical data with sources. Prefer 5-7 distinct data points. Each must have a hybrid citation. Data should be current (within the past year).

### 3. Government Programs Named
At least 1 government program named with: official name, what it offers, deadlines, portal URLs. Load known programs from `config/project.json` → `regulatory`.

### 4. Industry-Specific Focus
Article must target specific industries (not generic "all SMEs"). Check that named industries appear at least 3 times. Load target industries from `config/project.json` → `audience.industries`.

### 5. Actionable Steps
Must include:
- 1+ numbered step-by-step list
- 1+ specific URL to a portal or service
- 1+ deadline or timeframe
- Required documents or eligibility criteria

### 6. Local Market Context
Verify:
- Local currency values (from `config/project.json` → `market.currency`), never USD or generic
- References to local agencies from config
- Local regulations and compliance requirements
- Market-specific examples

### 7. Links
- **Internal**: 2-3 links to brand content with natural anchor text
- **External**: 1-2 links to government portals or authoritative sources

### 7b. References Section
All bracketed citation letters `[a]`, `[b]`, `[c]` listed at end of article with source name and URL.

### 8. CTA
- Positioned in conclusion section
- Natural connection to the article topic
- Mentions brand/product from config
- 2-4 sentences, helpful not salesy

### 9. SEO Optimized
- Title ≤ 60 characters with primary keyword
- Meta description 150-160 characters with keyword + CTA
- Primary keyword in first paragraph and at least one H2
- Proper heading hierarchy H1 → H2 → H3

### 10. TL;DR Summary
Immediately after hook. 3-5 bullet points with bold labels. Specific data (currency/percentage/deadline). Active voice, scannable.

### 11. FAQ Section
5-7 questions near end, before CTA. Must include: 1× "What…", 1× "How…", 1× "When…/deadline", 1× "How much…/amount". Direct answers 2-4 sentences each.

### 12. Tables for Data
At least 1 table if data warrants it. Use for: comparisons, multi-attribute data, step-by-step processes.

### 13. Active Voice Throughout
Minimize passive constructions. Check for: "can be", "was", "were", "is being" + past participle. Address reader directly with "you" and "your".

### 14. Professional Tone
Conversational but professional. Clear, simple explanations. Confident expertise. No corporate jargon, no aggressive sales language, no generic platitudes.

### 15. Optimal Length & Structure
- Word count: 1,200-1,800 words (target 1,500)
- Paragraphs: 2-3 sentences max
- Structure: Hook (100-150w) → TL;DR (50-75w) → Body (600-900w) → Actionable (150-250w) → FAQ (200-300w) → Conclusion+CTA (100-150w)

## Tier 2: Market Content (12 Points)

Same as Tier 1 with these differences:

- **Check 2**: 3-5 statistics acceptable (vs 5-7). Platform and industry data sources OK.
- **Check 3**: Replaced by **Industry Sources Cited** — cite platforms, associations, research firms instead of government programs. 3-5 statistics from industry data.
- **Check 5**: Commercial platform URLs acceptable, not limited to government portals.
- **Check 7**: Industry and platform sites OK for external links, not just government domains.
- **Check 12**: Tables recommended but not required.
- **Check 15**: Word count 1,000-1,500 words.
- Checks 13 and 14 combined into a single check.

## Critical Failures (Either Tier)

Any of these means automatic failure regardless of score:
- No statistics at all
- No local market context
- No actionable steps
- No TL;DR summary
- No FAQ section
- Excessive passive voice throughout
- Tier 1 only: No government programs named
- Tier 2 only: No industry sources cited

## Scoring Guide

**Tier 1**: 15/15 Excellent → 14/15 Great → 13/15 Good (pass) → ≤12/15 Needs revision
**Tier 2**: 12/12 Excellent → 11/12 Great → 10/12 Good (pass) → ≤9/12 Needs revision

## Review Output Format

Present results as:

```
ARTICLE REVIEW
==============
Tier: [1 or 2]
Score: [X]/[15 or 12] ([percentage]%)
Status: [APPROVED / NEEDS REVISION]

CHECKS:
  1. Hook with specific data       [PASS/FAIL] — [brief note]
  2. Statistics (3+)               [PASS/FAIL] — [count found]
  ...

FEEDBACK:
- [Specific issue and how to fix it]
- [Another issue]

RECOMMENDATION:
[Approve for publishing / Revise with specific guidance]
```

For detailed check specifications, see `references/checklist-details.md`.
