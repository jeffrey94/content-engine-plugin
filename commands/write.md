---
description: Write a full SEO-optimized blog article
argument-hint: [topic or brief-path]
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash(date:*, mkdir:*, wc:*)
---

# Writer Agent

Write a high-quality, SEO-optimized blog article from a content brief or a topic description.

## Setup

1. Read `config/project.json` for business context, tone, CTA, market details.
2. Read `config/content_pillars.json` for pillar alignment.
3. Read `config/seo_keywords.json` for keyword targets.
4. Load the content-style skill for formatting standards.
5. If `$ARGUMENTS` is a file path, read the brief. If it's a topic description, use it directly.
6. Get today's date and create output folder: `data/drafts/YYYYMMDD/`.

## Step 1: Research Evaluation

If a brief or prior research is provided:
1. **Check data freshness** — is the research within 7 days?
2. **Check topic coverage** — does it have enough statistics, programs, sources?
3. **Decision matrix**:
   - Data fresh + complete → Use as-is, proceed to writing
   - Data fresh + gaps → Research specific gaps with WebSearch/WebFetch
   - Data stale → Re-research the topic online before writing
   - No research provided → Full research phase required

### Research Workflow (when needed)

Use WebSearch and WebFetch to gather:
- 5-7 verified statistics with local currency or percentages
- 2-3 government programs (Tier 1) or industry sources (Tier 2)
- 3-5 official portal URLs or authoritative source links
- Recent news context (within 4 weeks)
- Industry-specific data relevant to target audience

Always verify statistics across at least 2 sources. Never fabricate data.

## Step 2: Writing

Apply the content-style skill throughout. Follow the article structure:

### Hook (100-150 words)
Open with a specific fact — local currency value, percentage, or surprising data point. Cite a credible, recent source. Create curiosity or urgency. Active voice.

### TL;DR (50-75 words)
Immediately after hook. 3-5 bullet points with bold labels:
- **Key fact**: specific data
- **Action**: what to do
- **Deadline**: if applicable
- **Benefit**: quantified outcome

### Body Sections (600-900 words)
3-5 sections with H2 headers that include keywords. Short paragraphs (2-3 sentences max). Statistics and data throughout. Use tables for comparisons and multi-attribute data.

**Citation style**: Hybrid format.
- First mention: "According to [Source Name], [statistic] [a]"
- Subsequent: "[statistic] [a]"

### Actionable Steps (150-250 words)
Numbered list with:
- Specific URLs to portals or services
- Step-by-step processes
- Deadlines and timeframes
- Required documents or eligibility

### FAQ Section (200-300 words)
5-7 questions in search-friendly format. Must include:
- 1+ "What is/are…"
- 1+ "How do I/can I…"
- 1+ "When is…" or deadline question
- 1+ "How much…" or amount question

Direct answers, 2-4 sentences each, with specific data.

### Conclusion + CTA (100-150 words)
Summarize 2-3 key takeaways. Soft CTA connecting the article topic to the brand — load angles from `config/project.json` → `cta`. Helpful, not salesy.

### References
List all sources at the end:
```
[a] Source Name - URL
[b] Source Name - URL
```

## Step 3: Quality Self-Check

Before saving, validate against the quality checklist:

**Tier 1 (Government)** — target 15/15, minimum 13/15:
- [ ] Hook with specific data
- [ ] 3+ statistics with local currency
- [ ] Government programs named
- [ ] Industry-specific focus
- [ ] Actionable steps with URLs
- [ ] Local market context
- [ ] Internal links (2+) and external links (1+)
- [ ] References section
- [ ] Soft CTA
- [ ] SEO optimized (title ≤60, meta 150-160)
- [ ] TL;DR summary
- [ ] FAQ section
- [ ] Tables for data
- [ ] Active voice throughout
- [ ] Word count 1,200-1,800

**Tier 2 (Market)** — target 12/12, minimum 10/12:
Same checks but: industry sources instead of government programs, 3-5 statistics acceptable, word count 1,000-1,500.

If the self-check score is below the minimum, revise the article to address gaps before saving.

## Step 4: Save Output

Save the article as markdown with YAML frontmatter to `data/drafts/YYYYMMDD/{article-slug}.md`:

```yaml
---
title: "Article Title (≤60 chars)"
meta_description: "150-160 char description with keyword and CTA"
primary_keyword: "target keyword"
secondary_keywords: ["kw1", "kw2", "kw3"]
content_pillar: "Pillar name"
content_type: "government|market"
quality_tier: 1
target_industries: ["Industry1", "Industry2"]
word_count: 1350
date_created: "YYYY-MM-DD"
author: "AI Writer"
version: "v1"
self_check_score: "14/15"
---

[Article content in markdown]
```

Also save a companion metadata file as `{article-slug}_metadata.json` with:
- All frontmatter fields
- Sources list with URLs
- Internal and external link inventory
- Quality self-assessment details

## Content Type Templates

**Government (Tier 1)**: Hook → TL;DR → Body (3-5 H2) → Actionable Steps → FAQ → CTA → References

**Market Pulse**: Hook → TL;DR → "What's Driving This" → Industry Impact → How to Capitalize → FAQ → CTA → References

**Operational Guide**: Hook → TL;DR → Feature Comparison Table → Cost Breakdown → Recommendations → Implementation Steps → FAQ → CTA → References

**Success Story**: Hook → TL;DR → Background → Challenge → Solution → Results Table → Lessons → FAQ → CTA → References

## Important Reminders

- Apply the content-style skill for tone and formatting
- Apply the research-sources skill for source evaluation
- Quality over speed — a 14/15 article is worth the extra effort
- Local market context is critical — never use generic international examples
- File naming: use TODAY's date for the folder, topic slug for the filename
