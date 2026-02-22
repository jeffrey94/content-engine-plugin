---
description: Create content briefs from research topics
allowed-tools: Read, Write, Glob, Grep, WebSearch, WebFetch, Bash(date:*, mkdir:*, ls:*)
---

# Content Strategist

Evaluate trending topics from research output and create 2-3 detailed content briefs.

## Setup

1. Read `config/project.json` for business context, audience, CTA angles.
2. Read `config/content_pillars.json` for content strategy.
3. Read `config/seo_keywords.json` for keyword targets.
4. Read `config/quality_checklist.json` for quality standards.
5. Find the most recent research file in `data/research/` (or use the file specified by the user).
6. Get today's date and create output folder: `data/briefs/YYYYMMDD/`.

## Evaluation Framework

Score each research topic across 5 dimensions:

### 1. Business Alignment (40% weight)
- Content pillar fit
- Audience relevance to `config/project.json` → `audience`
- Differentiation potential (can we add unique value?)
- Natural brand connection for CTA

### 2. SEO Potential (30% weight)
- Search volume indicators
- Keyword competition level
- Ranking opportunity (gaps in current SERP)
- SERP feature targets (featured snippet, PAA)
- Keyword opportunity score from research

### 3. Timeliness & Urgency (20% weight)
- Time sensitivity (deadlines, policy changes)
- Newsworthiness (recent announcements)
- Is this a refresh of existing content or a new article?

### 4. Content Quality Potential (10% weight)
- Data richness (enough for 3+ statistics?)
- Actionability (specific steps readers can take?)
- Industry specificity (not generic?)

### 5. Content Format Strategy (bonus)
- Match format to SERP landscape and search intent
- Consider: listicle, guide, comparison, news analysis

## Selection Criteria

When selecting 2-3 topics:
- **Must select** any time-sensitive topic (upcoming deadline)
- **Ensure variety**: mix of content pillars, difficulty levels, funnel stages
- **Maintain balance**: respect the government/market content split from config
- **Prioritize** SERP feature opportunities and topic cluster gaps

## Keyword Validation Step

After selecting 2-3 topics but BEFORE writing the brief, validate the primary keyword for each selected topic. This step prevents keyword-article mismatches where the keyword's SERP landscape doesn't match the planned article's angle.

### A: Resolve Candidate Keyword
1. If research output included a `suggested_keyword` (from keyword fitness check), use it as the primary candidate
2. Otherwise, pick the best-fit keyword from `config/seo_keywords.json` or `config/content_pillars.json` keywords

### B: SERP Validation
Search the candidate keyword (using WebSearch with market context from `config/project.json`):
1. Examine the top 5 organic results:
   - **Angle match**: Do 3+ results address the same angle as the planned article?
   - **Intent match**: Is the dominant search intent (informational/commercial/transactional) aligned with the planned content type?
   - **Competitor type**: Are results articles, encyclopedias, product pages, or tools? Does this match what we're writing?
2. Classify the SERP fit:
   - `strong_match`: 4-5 of top 5 results align with the article angle
   - `partial_match`: 2-3 of top 5 results align
   - `mismatch`: 0-1 of top 5 results align (e.g., SERP dominated by medical authority sites but we're writing a practical guide)

### C: Handle Mismatches
If SERP validation returns `partial_match` or `mismatch`:
1. Generate 2-3 alternative keywords from:
   - The article title's core terms (often the best keyword is hiding in the title itself)
   - PAA questions from the research output
   - Related searches from the research output
2. Run the same SERP validation (Step B) on each alternative
3. Pick the keyword with the strongest SERP fit
4. If no keyword achieves `strong_match`, use the best `partial_match` and note the limitation

### D: Document the Decision
Record the validation result in the brief output — this makes keyword choices traceable and reviewable.

## Content Brief Output

For each selected topic, create a comprehensive brief and save as JSON to `data/briefs/YYYYMMDD/brief_{topic_slug}.json`:

```json
{
  "brief_id": "topic-slug",
  "created_date": "YYYY-MM-DD",
  "topic": "Full article title",
  "primary_keyword": "validated keyword from Keyword Validation Step",
  "keyword_validation": {
    "original_keyword": "keyword before validation",
    "original_source": "seo_keywords|content_pillars|research_suggested",
    "serp_match": "strong_match|partial_match|mismatch",
    "serp_dominant_type": "e.g., medical encyclopedias, practical guides, product pages",
    "validated_keyword": "the keyword after validation (may be same as original)",
    "validation_rationale": "Why this keyword was kept or changed",
    "alternatives_considered": [
      {"keyword": "alt keyword", "serp_match": "result", "reason": "why kept or rejected"}
    ]
  },
  "secondary_keywords": ["kw1", "kw2", "kw3"],
  "content_pillar": "Pillar name",
  "content_type": "government|market",
  "quality_tier": 1,
  "recommended_hook": {
    "selected_option": "A",
    "hook_type": "Pain Point|Opportunity|Curiosity",
    "opening_paragraph": "Full hook paragraph",
    "emotional_trigger": "Description",
    "rationale": "Why this hook works"
  },
  "all_hook_options": [
    {
      "option": "A",
      "hook_type": "Type",
      "opening_sentence": "First sentence",
      "full_paragraph": "Complete hook",
      "emotional_trigger": "Trigger",
      "why_it_works": "Explanation",
      "best_for": "Audience segment"
    }
  ],
  "target_audience": {
    "primary_persona": {
      "name": "Persona name",
      "demographics": "Description",
      "pain_points": ["point1", "point2"],
      "current_knowledge_level": "Basic|Intermediate|Advanced",
      "desired_outcome": "What they want"
    }
  },
  "required_statistics": [
    {"stat": "Description", "source": "Source", "priority": "must-have|nice-to-have"}
  ],
  "government_programs": ["Program names if Tier 1"],
  "industry_sources": ["Source names if Tier 2"],
  "article_structure": {
    "h2_sections": ["Section 1 title", "Section 2 title"],
    "tables_needed": ["Description of table"],
    "actionable_steps_focus": "What specific actions"
  },
  "seo_strategy": {
    "title_options": ["Title 1 (≤60 chars)", "Title 2"],
    "meta_description": "150-160 chars with keyword and CTA",
    "serp_feature_target": "featured_snippet|paa|none",
    "paa_questions": ["Q1", "Q2"]
  },
  "cta_angle": "Natural connection to brand",
  "word_count_target": {"min": 1200, "max": 1500},
  "funnel_stage": "awareness|consideration|decision",
  "priority": "high|medium",
  "deadline": "If time-sensitive"
}
```

Also include a summary of rejected topics with brief reasons.

## Content Type Templates

### Government Content (Tier 1)
Traditional article: Hook → TL;DR → Body (3-5 H2s) → Actionable Steps → FAQ → CTA.
15-point checklist. Target: 1,200-1,800 words.

### Market Pulse (Tier 2)
Trend analysis: Hook → TL;DR → "What's Driving This" → Industry Impact → How to Capitalize → FAQ → CTA.
12-point checklist. Target: 1,000-1,500 words.

### Operational Guide (Tier 2)
Platform/tool comparison: Hook → TL;DR → Feature Comparison Table → Cost Breakdown → Recommendations → Implementation Steps → FAQ → CTA.
12-point checklist. Target: 1,000-1,500 words.

### Success Story (Tier 2 — max 1 per quarter)
Case study: Hook → TL;DR → Background → Challenge → Solution → Results (before/after table) → Lessons → FAQ → CTA.
12-point checklist. Target: 1,000-1,500 words.

## 50/50 Content Mix

Maintain the content split from `config/project.json` → `content.content_split`. If recent briefs skew toward one type, prioritize the underrepresented type.
