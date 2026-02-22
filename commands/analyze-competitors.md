---
description: Analyze competitors for a keyword or article
argument-hint: [keyword or article-path]
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash(date:*, mkdir:*), AskUserQuestion
---

# Competitive Analysis Agent

Compare a blog article against top-ranking Google results for target keywords. Identify content gaps, SEO opportunities, and differentiation points across multiple SERPs.

## Setup

1. Read `config/project.json` for market context and business details.
2. Determine inputs:
   - If `$ARGUMENTS` is a file path:
     - Read the article and parse YAML frontmatter.
     - Extract `primary_keyword` → main keyword.
     - Extract `secondary_keywords` array → additional keywords.
     - Build keyword list: `[primary_keyword] + secondary_keywords`.
     - If `secondary_keywords` has more than 5 entries, keep only the first 5.
   - If `$ARGUMENTS` is a keyword string: use it as the sole target keyword, and optionally find a matching draft in `data/drafts/`. (Single-keyword mode — skip all multi-keyword sections below.)
3. Get today's date and create output folder: `data/competitive_analysis/YYYYMMDD/`.
4. **Confirm keywords with user** (article path mode only): Present the keyword list and ask the user to confirm or modify it before running searches. Example:

   > I found these keywords in the article frontmatter:
   > 1. **bleeding gums** (primary)
   > 2. bleeding gums when brushing
   > 3. bleeding gums treatment
   > 4. stop bleeding gums
   >
   > Shall I search all 4 keywords, or would you like to add/remove any?

## Step 1: Read Our Article

If an article is available, extract:
- Word count
- Main topics covered (H2 sections)
- Statistics count and specifics
- Government programs or industry sources mentioned
- Article structure (TL;DR, FAQ, tables present?)
- Link inventory (internal + external)
- CTA approach
- SEO elements: meta title (character count), meta description (character count), primary keyword placement, H2/H3 keywords

## Step 2: Fetch Competitor Content

### Multi-keyword mode (article path with secondary keywords)

For each keyword in the confirmed keyword list:
1. Use ~~search api to search for the keyword and get the top 10 organic results. Use the `location` from `config/project.json` → `market` field if available.
2. Store results keyed by keyword (keyword → list of {rank, title, url, domain}).

Run searches for independent keywords in parallel where possible.

After all searches complete:
- Build a **deduplicated URL set** across all keyword SERPs.
- For each unique competitor URL, WebFetch the page content **once** (even if it appears in multiple SERPs).
- Extract from each page:
  - Title and meta description (with character counts)
  - Word count
  - Main topics covered
  - Statistics and data points
  - Government programs or industry sources
  - Article structure (FAQ, tables, TL;DR)
  - Unique angles or content we don't have
  - Source quality (government, news, blog)
  - H1 tag, keyword placement, power words in title

If WebFetch fails for a URL, note it as "Not analyzed" and continue.

### Single-keyword mode (keyword string argument)

Use ~~search api to search for the target keyword and get the top 10 organic results.

For each competitor URL in the top 10:
1. WebFetch the page content
2. Extract the same fields listed above.

If WebFetch fails for a URL, note it as "Not analyzed" and continue.

## Step 3: Comparative Analysis

Analyze across 9 dimensions:

### 1. Topic Coverage
- What topics do competitors cover that we don't?
- What's unique to our article?
- What are must-haves that most competitors include?

### 2. Statistics & Data
- Count of statistics per competitor vs ours
- Unique statistics we're missing
- Data recency comparison

### 3. Government Programs / Industry Sources
- Which programs/sources appear most frequently across competitors?
- Are we missing commonly-referenced ones?

### 4. Article Structure
- % of competitors with FAQ sections
- % with data tables
- % with TL;DR or summary sections
- Average word count across competitors

### 5. Actionable Content
- Do competitors provide specific steps, URLs, deadlines?
- How do our actionable sections compare?

### 6. Unique Angles
- What differentiators does each competitor have?
- What's our unique differentiation to preserve?

### 7. Meta Tags & CTR Analysis
- Title patterns across top rankers (length, power words, format)
- Meta description patterns
- CTR optimization opportunities

### 8. SERP Features
- Who owns the featured snippet (if any)?
- What PAA questions appear?
- What related searches show?
- In multi-keyword mode: note which SERP features appear for which keywords.

### 9. Keyword Optimization
- Keyword placement patterns (title, H1, H2, first paragraph)
- Secondary and LSI keywords used by competitors
- Keyword variations we're missing
- In multi-keyword mode: which competitors are optimized for multiple keywords from our list?

## Step 4: Generate Report

Save as markdown to `data/competitive_analysis/YYYYMMDD/{primary_keyword_slug}_analysis.md`:

```markdown
# Competitive Analysis: [Primary Keyword]
Date: YYYY-MM-DD
Keywords analyzed: [count]

## Executive Summary

| Metric | Our Article | Top 10 Average | Best Competitor |
|--------|------------|----------------|-----------------|
| Word Count | X | Y | Z |
| Statistics | X | Y | Z |
| Programs/Sources | X | Y | Z |
| Has FAQ | Yes/No | X% | — |
| Has Tables | Yes/No | X% | — |
| Has TL;DR | Yes/No | X% | — |
| SEO Score | X/5 | Y/5 | Z/5 |
| Keywords Covered | X/Y | — | Z/Y |

## SERP Overview by Keyword

(Multi-keyword mode only. Omit this section in single-keyword mode.)

### "bleeding gums" (primary)
| Rank | Title | URL | Domain |
|------|-------|-----|--------|
| 1 | ... | ... | ... |

### "bleeding gums when brushing" (secondary)
| Rank | Title | URL | Domain |
|------|-------|-----|--------|
| 1 | ... | ... | ... |

[Repeat for each keyword searched]

## Cross-Keyword Competitor Matrix

(Multi-keyword mode only. Omit this section in single-keyword mode.)

| Competitor | bleeding gums | ...when brushing | ...treatment | Keywords |
|-----------|:---:|:---:|:---:|:---:|
| clevelandclinic.org | #1 | #3 | — | 2/4 |
| colgate.com | #4 | #2 | #1 | 3/4 |

Competitors appearing for 3+ keywords are the **strongest competitors** — prioritize analyzing their content.

## Competitor Breakdown

### Rank 1: [Title]
- URL: [url]
- Word count: X
- Key topics: [list]
- Statistics: [count]
- Strengths: [what they do well]
- SEO: Title [X chars], Meta [Y chars]
- Appears in SERPs for: [list of keywords where this URL ranked]

[Repeat for each analyzed competitor]

## Consolidated Gap Analysis

### Missing Topics (by priority)
- **HIGH**: [Topics 70%+ competitors cover that we don't — across all SERPs]
- **MEDIUM**: [Topics 30-70% cover]
- **LOW**: [Topics <30% cover]

### Missing Statistics
- [Stat competitors have that we don't]

### Missing Programs/Sources
- [Programs or sources we should add]

### Structural Improvements
- [FAQ, tables, TL;DR changes needed]

### SEO Improvements
- Meta title: [recommendations]
- Meta description: [recommendations]
- Keyword placement: [gaps]
- SERP features: [opportunities — note which keyword each opportunity is for]
- Cross-keyword optimization: [recommendations for ranking across multiple keywords]

## Our Strengths (Preserve These)
- [What differentiates our article positively]

## Recommended Actions

### Priority 1 (Must Do)
- [Actions that address HIGH gaps]

### Priority 2 (Should Do)
- [Actions that address MEDIUM gaps]

### Priority 3 (Nice to Have)
- [Actions that address LOW gaps]

## Competitors Not Analyzed
- [URLs that failed to load]
```

## Analysis Guidelines

**Scoring**:
- **Strong**: We match or exceed 70%+ of competitors on this dimension
- **Competitive**: We're in the 30-70% range
- **Needs Improvement**: We're below 30% of competitors

**Focus on actionable insights** — every gap identified should come with a specific recommendation for what to add or change. Quality over quantity — a few high-impact improvements beat a long list of minor tweaks.

**Multi-keyword priority** — when reporting gaps, note which keyword's SERP revealed the gap. Gaps visible across multiple keyword SERPs are higher priority than gaps from a single SERP.
