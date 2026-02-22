---
name: research-sources
description: >
  Guide research methodology and source selection for content topics. Use when
  the user asks to "research topics", "find trending news", "scan for content ideas",
  "verify sources", or needs guidance on which sources to trust, how to evaluate
  source quality, or where to find market-specific data.
version: 0.2.0
---

# Research Sources & Methodology

Guide for finding, evaluating, and citing sources for blog content. All source lists are loaded from `config/project.json` → `research_sources` and `regulatory.agencies`.

## Source Categories

### 1. Government Portals & Official Sources
Load from `config/project.json` → `regulatory.agencies`. Use for:
- Policy announcements and compliance deadlines
- Official program details, eligibility, and registration
- Economic data and statistics
- Tax and regulatory changes

### 2. Primary News Websites
Load from `config/project.json` → `research_sources.front_pages` and `business_sections`. Use for:
- Trending topic discovery
- Breaking policy announcements
- Industry news and analysis

### 3. Macro-Economic & Financial Sources
Load from `config/project.json` → `research_sources.macro_economic`. Use for:
- Exchange rates and monetary policy
- Commodity prices affecting industries
- Trade and GDP data
- Investment flows and FDI

### 4. Industry & Market Sources (Non-Government)
Load from `config/project.json` → `research_sources`:
- **Platform data** (`platform_sources`): e-commerce reports, delivery insights, professional network data
- **Industry associations** (`industry_associations`): federation surveys, SME reports
- **Research firms** (`research_firms`): bank SME surveys, consumer research

## Research Methodology

### For Government/Policy Topics (Tier 1 Content)

1. **Scan front pages** — WebSearch for recent policy announcements using keywords from `config/project.json` → `research_sources.search_keywords`
2. **Deep-dive official sources** — WebFetch government portals to extract specific program details, eligibility, deadlines, URLs
3. **Verify statistics** — Cross-reference data points across at least 2 sources
4. **Extract key data**: currency values, percentages, dates, program names, portal URLs

### For Market/Industry Topics (Tier 2 Content)

1. **Platform data research** — WebSearch for e-commerce, delivery, professional platform reports
2. **Industry association reports** — WebSearch for federation surveys, SME reports
3. **Economic indicators** — WebSearch for wage data, employment stats, consumer research
4. **Technology & tools data** — WebSearch for accounting, e-commerce, job portal reports

### Decision Tree

```
Is the topic about government policy, compliance, or official programs?
  YES → Government portals + official news → Tier 1
  NO  → Is it about market trends, platforms, or industry data?
    YES → Platform data + industry associations → Tier 2
    MIXED → Use both source categories → Choose tier by primary angle
```

## Search Keywords

Load from `config/project.json` → `research_sources.search_keywords`:
- `base`: core industry keywords
- `financing`: funding and financing keywords
- `compliance`: regulatory and compliance keywords
- `industry`: sector-specific keywords

Always append the current year to search queries for freshness.

## Source Quality Evaluation

### Trusted (use confidently)
- Government portals and official agency websites
- Central bank publications
- Established local news outlets
- Verified industry associations
- Domains listed in `config/project.json` → `market.trusted_news_domains`

### Questionable (verify with a second source)
- Blogs and personal websites
- Social media posts
- Press releases without corroboration
- Content aggregator sites

### Unreliable (do not use)
- Unverified websites
- International sites writing about the local market without local expertise
- Information older than 12 months for policy topics
- Sites without clear authorship

## Freshness Requirements

- **Policy/compliance topics**: Data must be within 4 weeks
- **Market trends**: Data within 3 months acceptable
- **Evergreen guides**: Data within 12 months acceptable, but verify nothing has changed
- Reject any topic where the core data is stale

## Citation Format

Use hybrid citation style:
- First mention: full inline attribution + bracketed letter `[a]`
- Subsequent mentions: letter only `[a]`
- References section at end: `[a] Source Name - URL`

## Tool Failure Handling

If WebFetch is denied for a URL:
1. Try WebSearch with the page title or key phrases
2. Look for the same data on alternative official sources
3. Note in output that direct source verification was limited
4. Never fabricate data — if a statistic cannot be verified, exclude it
