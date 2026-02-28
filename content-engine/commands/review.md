---
description: Validate an article against the quality checklist
argument-hint: [article-path]
allowed-tools: Read, Grep, Glob, Write, Bash(wc:*, date:*)
---

# Article Reviewer

Validate an article against the content quality checklist and produce a detailed review report.

## Setup

1. Read the article at `$ARGUMENTS` (or find the most recent draft in `data/drafts/`).
2. Read `config/project.json` for market context, currency, agencies, audience.
3. Read `config/quality_checklist.json` for check specifications.
4. Load the content-quality-checklist skill for scoring framework.

## Determine Tier

Parse the article's YAML frontmatter:
- If `content_type: "government"` or `quality_tier: 1` → **Tier 1** (15-point, pass: 13/15)
- If `content_type: "market"` or `quality_tier: 2` → **Tier 2** (12-point, pass: 10/12)
- If no frontmatter, infer from content: government programs mentioned → Tier 1, otherwise → Tier 2

## Run Checks

### Check 1: Hook with Specific Data
Examine the first 2 paragraphs. Look for:
- A local currency value (from `config/project.json` → `market.currency`)
- A percentage or numerical data point
- A credible source citation
- **PASS** if at least one specific data point with source exists in the opening.

### Check 2: Statistics Count
Search the full article for:
- Currency values matching the local currency pattern
- Percentages (X%)
- Numerical data with source attribution
- **Tier 1 PASS**: 5+ distinct data points (minimum 3)
- **Tier 2 PASS**: 3+ distinct data points

### Check 3: Government Programs / Industry Sources
**Tier 1**: Search for named government programs from `config/project.json` → `regulatory.known_programs`. At least 1 with official name, what it offers, and a portal URL.
**Tier 2**: Search for named industry sources — platforms, associations, research firms. At least 3 with attribution.

### Check 4: Industry-Specific Focus
Search for industry names from `config/project.json` → `audience.industries`. At least 3 mentions of specific industries (not generic "SMEs" or "businesses").

### Check 5: Actionable Steps
Look for:
- At least 1 numbered or bulleted step list
- At least 1 specific URL (https://)
- At least 1 deadline or timeframe
- **PASS** if all three present.

### Check 6: Local Market Context
Verify:
- Local currency used (not USD or generic)
- Local agencies or regulatory bodies referenced
- Local regulations or compliance mentioned
- **PASS** if currency is local AND at least 1 local agency referenced.

### Check 7: Links
Count:
- Internal links (to brand content): need 2+
- External links (to authoritative sources): need 1+
- **PASS** if both minimums met.

### Check 7b: References Section
Check for a references section at the end with `[a]`, `[b]`, etc. mapped to source names and URLs. **PASS** if present and all citation letters are mapped.

### Check 8: CTA
Look for a call-to-action in the conclusion section:
- Mentions the brand or product from config
- Natural connection to article topic
- Helpful, not salesy language
- **PASS** if CTA exists and is not aggressive.

### Check 9: SEO
- Title length: ≤ 60 characters (from frontmatter `title`)
- Meta description: 150-160 characters (from frontmatter `meta_description`)
- Primary keyword in: title, first paragraph, at least one H2
- Heading hierarchy: H1 → H2 → H3 (no skipped levels)
- **PASS** if title ≤ 60, meta 150-160, keyword in first paragraph.

### Check 10: TL;DR Summary
Look for a TL;DR section after the hook with:
- 3-5 bullet points
- Bold labels
- Specific data
- **PASS** if present with at least 3 bullets containing data.

### Check 11: FAQ Section
Look for a FAQ section near the end (before CTA):
- 5-7 questions in search format
- Must include: 1× "What", 1× "How", 1× "When/deadline", 1× "How much/amount"
- **PASS** if 5+ questions with at least 3 of the 4 required types.

### Check 12: Tables (Tier 1 only)
Look for at least 1 markdown table if the article contains comparison data or multi-attribute information. **PASS** if a table exists or data doesn't warrant one.

### Check 13: Active Voice (Tier 1 only)
Scan for passive constructions: "can be", "was [verb]ed", "were [verb]ed", "is being [verb]ed", "has been [verb]ed". Count instances. **PASS** if passive constructions are < 15% of sentences.

### Check 14: Professional Tone (Tier 1 only)
Scan for:
- Salesy language ("amazing", "incredible", "guaranteed", "act now")
- Corporate jargon without explanation
- Generic platitudes ("in today's fast-paced world")
- **PASS** if none of the above detected.

### Check 15: Word Count & Structure (Tier 1 only)
- Count words (excluding frontmatter)
- **Tier 1 PASS**: 1,200-1,800 words
- **Tier 2**: 1,000-1,500 words (combined with checks 13-14)

## Critical Failures

Flag automatic failure if ANY of these are true:
- Zero statistics in the entire article
- No local currency used anywhere
- No actionable steps
- No TL;DR section
- No FAQ section
- Tier 1: No government programs named
- Tier 2: No industry sources cited

## Output

Present the review in this format:

```
ARTICLE REVIEW
==============
Article: [filename]
Tier: [1 or 2]
Score: [X]/[15 or 12] ([percentage]%)
Status: [APPROVED / NEEDS REVISION]

CHECKS:
  1.  Hook with specific data       [PASS/FAIL] — [note]
  2.  Statistics (3+)               [PASS/FAIL] — [X found]
  3.  Gov Programs / Industry Src   [PASS/FAIL] — [names found]
  4.  Industry-specific focus       [PASS/FAIL] — [X mentions]
  5.  Actionable steps              [PASS/FAIL] — [note]
  6.  Local market context          [PASS/FAIL] — [currency + agencies]
  7.  Links (internal + external)   [PASS/FAIL] — [X int, Y ext]
  7b. References section            [PASS/FAIL] — [X refs listed]
  8.  CTA                           [PASS/FAIL] — [note]
  9.  SEO optimized                 [PASS/FAIL] — [title len, meta len]
  10. TL;DR summary                 [PASS/FAIL] — [X bullets]
  11. FAQ section                   [PASS/FAIL] — [X questions]
  12. Tables for data               [PASS/FAIL] — [X tables]
  13. Active voice                  [PASS/FAIL] — [X% passive]
  14. Professional tone             [PASS/FAIL] — [issues if any]
  15. Word count & structure        [PASS/FAIL] — [X words]

CRITICAL FAILURES: [None / List]

FEEDBACK:
- [Specific issue #1 and how to fix it]
- [Specific issue #2 and how to fix it]

RECOMMENDATION:
[APPROVED for publishing / REVISE: specific guidance on what to improve]
```

Save the review to `data/drafts/YYYYMMDD/{article-slug}_review.md`.
