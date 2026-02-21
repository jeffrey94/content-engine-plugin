# Article Analysis Framework

## Purpose

Defines how to extract content signals from a blog article for image generation. Used in Step 2 of the workflow.

## Input

Article markdown file from `data/drafts/YYYYMMDD/{article-slug}.md`

## Extraction Steps

### 1. Parse YAML Frontmatter

Extract these fields (if present):

| Field | Used For | Required |
|---|---|---|
| `title` | Cover hero text, social card headlines | Yes |
| `primary_keyword` | Cover hero subtitle, SEO alignment | Yes |
| `secondary_keywords` | Additional context signals | No |
| `content_pillar` | Auto-selection matrix primary signal | Yes |
| `hook_type` | Auto-selection tiebreaker | No |
| `meta_description` | Alternative subtitle text | No |

If `content_pillar` is missing from frontmatter, infer it from article content using the four pillars:
- Policy & Compliance (government, regulation, tax, compliance keywords)
- Funding & Financing (loan, financing, cash flow, RM keywords)
- Industry Opportunities (market, growth, investment, infrastructure keywords)
- Practical Guides (how-to, guide, comparison, step-by-step keywords)

### 2. Extract Key Statistics

Scan the full article body for:

- **RM values**: Look for patterns like `RM[0-9]`, `RM [0-9]`, `ringgit`. Capture the number and its context sentence.
- **Percentages**: Look for patterns like `[0-9]+%`, `percent`. Capture the number and its context.
- **Timeframes**: Look for specific dates, deadlines, year references.

Select the **top 3 most compelling statistics** based on:
1. Highest absolute RM value
2. Most surprising percentage (very high >80% or very low <10%)
3. Most time-sensitive deadline

### 3. Extract TL;DR Points

Look for a section starting with:
- `## TL;DR`
- `## Key Takeaways`
- `## Summary`
- `## At a Glance`

Extract each bullet point as a standalone takeaway. These become:
- Instagram carousel slide content
- Facebook card key stat candidates

If no TL;DR section exists, extract the **first sentence of each H2 section** as proxy takeaways (maximum 5).

### 4. Infer Visual Theme

Map the article topic to a visual illustration category:

| Topic Category | Visual Elements |
|---|---|
| Tax / Filing | Calculator, forms, documents, calendar, LHDN building |
| Financing / Loans | Money flow, growth arrows, piggy bank, coins, invoice |
| Technology / Digital | Devices, circuits, cloud, dashboard, code symbols |
| Infrastructure / Construction | Buildings, cranes, blueprints, maps, industrial |
| Export / Trade | Globe, shipping containers, airplane, ports |
| Compliance / Legal | Shield, checkmark, stamp, certificate, gavel |
| Tourism / Culture | Landmarks, traditional patterns, food, nature |
| General Business | Handshake, graphs, office, briefcase, growth chart |

### 5. Generate Core Benefit Statement

Distill the article's value into a single sentence answering: "After reading this, the SME owner will..."

Examples:
- "...know exactly how to file e-invoices before the March deadline"
- "...understand which government financing program fits their business"
- "...have a 5-step checklist for halal certification"

## Output

Save all extracted data as internal context for Steps 3-5. This data is NOT saved as a separate file -- it flows directly into the prompt assembly process.

Fields available for prompt templates:
- `{article_title}` -- from frontmatter
- `{primary_keyword}` -- from frontmatter
- `{content_pillar}` -- from frontmatter or inferred
- `{visual_theme}` -- inferred topic category
- `{topic_illustration_subject}` -- specific visual elements for this topic
- `{stat_1}`, `{stat_2}`, `{stat_3}` -- top 3 statistics with context
- `{compelling_stat}` -- single most compelling stat (for facebook-card)
- `{tl_dr_points}` -- list of takeaway bullets
- `{core_benefit}` -- single benefit sentence
- `{summary_headline}` -- punchy 8-word headline (generated for social cards)
- `{action_phrase}` -- CTA hint (generated for social cards)
