---
description: Research trending topics for content ideas
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash(date:*, mkdir:*)
---

# Research Agent

Find 5-10 trending topics in the configured market and filter for audience relevance.

## Setup

1. Read `config/project.json` to load business context, market, audience, and research sources.
2. Read `config/content_pillars.json` to understand content strategy.
3. Read `config/seo_keywords.json` to load keyword targets.
4. Get today's date and create the output folder: `data/research/YYYYMMDD/`.

**Critical**: Use TODAY's date for the folder name, not the topic's date.

## Research Workflow

### Step 0: Keyword & Competitor Gap Discovery
- Load primary and competitor keywords from `config/seo_keywords.json`
- WebSearch for each high-priority keyword to assess current SERP landscape
- Note which keywords have weak competition or missing content types

### Step 1: Trending Scan
- WebSearch using keywords from `config/project.json` → `research_sources.search_keywords` (append current year)
- WebFetch the front pages and business sections listed in `config/project.json` → `research_sources.front_pages` and `business_sections`
- Collect all headlines related to the target market/audience from the past 4 weeks
- **Reject** any topic where the core news is older than 4 weeks

### Step 2: Business Impact Filter
For each headline, answer these 4 questions:
1. Does this affect the target audience defined in `config/project.json` → `audience`?
2. Can it connect to at least one content pillar from `config/content_pillars.json`?
3. Is there enough data for 3+ statistics?
4. Is there an actionable angle (steps readers can take)?

Keep only topics that pass at least 3 of 4 filters.

### Step 2.5: SERP Feature & PAA Mining + Keyword Evaluation
For each surviving topic:
- WebSearch the likely primary keyword
- Note: Does a featured snippet exist? Who owns it?
- Extract "People Also Ask" questions (these become FAQ candidates)
- Note related searches (these become secondary keywords)
- **Keyword fitness check**: Compare the primary keyword's SERP against the planned article angle.
  - Do 3+ of the top 5 results cover the same angle as the planned article?
  - If the SERP is dominated by a different content type (e.g., medical encyclopedias when we're writing a practical guide), flag as a potential keyword mismatch.
  - When a mismatch is detected, check if PAA questions, related searches, or the topic title itself suggest a better-fitting keyword. If so, record it as `suggested_keyword` with `suggestion_rationale` in the output.

### Step 3: Deep-Dive Research
For each topic that passed Step 2:
- Determine source type: Government topic → use government portals. Market topic → use industry/platform sources.
- WebFetch official sources to extract: currency values, percentages, dates, program names, portal URLs
- Verify statistics across at least 2 sources
- Note full article URL, publication name, date, and author for citation

### Step 4: Classification & Ranking
For each topic:
1. **Classify**: Government (Tier 1) or Market (Tier 2)
2. **Assign content pillar** from `config/content_pillars.json`
3. **Rank** by: timeliness, data richness, SEO potential, audience relevance
4. **Balance check**: Maintain the content split from `config/project.json` → `content.content_split`
5. **Freshness check**: Reject anything with stale core data
6. **Cluster**: Group related topics, identify pillar vs supporting content roles

## Output Format

Save as JSON to `data/research/YYYYMMDD/research_YYYYMMDD_HHMMSS.json`:

```json
{
  "research_date": "YYYY-MM-DD",
  "timestamp": "ISO 8601",
  "market": "from config",
  "topics_found": 7,
  "content_type_split": {"government": 4, "market": 3},
  "topics": [
    {
      "rank": 1,
      "title": "Topic title",
      "content_type": "government|market",
      "content_pillar": "Pillar name",
      "trend_signal": "What triggered this topic",
      "key_data_points": [
        {"stat": "Currency or percentage", "source": "Source name", "date": "Date"}
      ],
      "target_audience": "Specific audience segment",
      "government_programs": ["Program names if applicable"],
      "content_angle": "Unique angle for the article",
      "seo_potential": {
        "primary_keyword": "keyword",
        "keyword_source": "content_pillars|seo_keywords|topic_title",
        "keyword_mismatch": false,
        "suggested_keyword": null,
        "suggestion_rationale": null,
        "search_intent": "informational|commercial|transactional",
        "competition": "low|medium|high",
        "serp_features": {"featured_snippet": true, "paa_questions": ["Q1", "Q2"]},
        "related_searches": ["search1", "search2"]
      },
      "sources": [
        {"name": "Source name", "url": "URL", "date": "Date", "type": "government|news|industry"}
      ],
      "funnel_stage": "awareness|consideration|decision",
      "topic_cluster_role": "pillar|supporting",
      "competitor_coverage": "high|medium|low|none",
      "refresh_candidate": false
    }
  ]
}
```

## Quality Checks

**Government topics (Tier 1)**: Must have at least 1 named government program, 3+ statistics with local currency, 1+ official portal URL.

**Market topics (Tier 2)**: Must have at least 3 industry data points, named platform/association sources, specific market figures.

## Tool Failure Handling

If WebFetch is denied for a URL:
1. Try WebSearch with the page title or key phrases
2. Look for the same data on alternative sources
3. Note in output that direct verification was limited
4. Never fabricate data — exclude unverifiable statistics
