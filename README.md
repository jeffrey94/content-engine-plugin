# Content Engine

AI-powered content marketing pipeline for creating SEO-optimized blog articles. Research trending topics, create content briefs, write articles, validate quality, and analyze competitors — all through slash commands in Claude Cowork.

## What It Does

A universal content marketing system that adapts to any business. Configure your brand once, then use natural commands to produce high-quality articles:

- **`/research`** — Scan news sources for 5-10 trending topics with statistics and data
- **`/brief`** — Evaluate topics and create detailed content briefs with hooks, keywords, and structure
- **`/write [topic]`** — Write a full 1,200-1,500 word SEO-optimized article
- **`/review [article]`** — Validate against a 15-point quality checklist
- **`/analyze-competitors [keyword]`** — Compare your article against top Google results
- **`/setup-brand`** — Guided setup for your business, audience, and content strategy

**Typical cost**: ~$5.80 per article | **Time**: 30-45 minutes end-to-end

## Getting Started

### 1. Install the Plugin

Accept the `.plugin` file in Claude Cowork.

### 2. Set Up Your Brand

On first session, the plugin auto-detects that you're new and walks you through setup. Or run `/setup-brand` manually. Setup takes ~10 minutes and configures:

- Business identity (name, services, market)
- Target audience (industries, pain points)
- Content pillars (3-4 topic themes)
- SEO keywords
- Tone and CTA style
- Research sources

### 3. Write Your First Article

**Quick start** (20 min): `/write How to [topic relevant to your audience]`

**Full pipeline** (45 min):
1. `/research` — find trending topics
2. `/brief` — create content briefs from research
3. `/write` — write article from brief
4. `/review` — validate quality

## Components

### Skills (4)

| Skill | Purpose |
|-------|---------|
| content-style | Tone, voice, formatting standards for all blog content |
| content-quality-checklist | 15-point (Tier 1) / 12-point (Tier 2) quality validation |
| content-visuals | Image prompt generation with 9 art styles and brand awareness |
| research-sources | Source evaluation methodology and research workflows |

### Commands (6)

| Command | What It Does |
|---------|-------------|
| `/research` | Scan news for trending topics with statistics |
| `/brief` | Create detailed content briefs from research |
| `/write [topic]` | Write a full SEO-optimized article |
| `/review [path]` | Validate article against quality checklist |
| `/analyze-competitors [kw]` | SERP analysis and content gap report |
| `/setup-brand` | Configure brand, audience, and strategy |

### MCP Servers (1)

| Server | Purpose |
|--------|---------|
| SerpAPI | Structured Google search results for competitive analysis |

## Setup

### Required Environment Variables

```bash
# For competitive analysis (required for /analyze-competitors)
export SERPAPI_API_KEY=your_key_here
```

Sign up at [serpapi.com](https://serpapi.com) — free tier includes 100 searches/month.

### Optional Environment Variables

```bash
# For image generation (only if using an API backend)
export GEMINI_API_KEY=your_key      # Google Gemini
export OPENAI_API_KEY=your_key      # DALL-E
export STABILITY_API_KEY=your_key   # Stable Diffusion
```

## Configuration Files

After running `/setup-brand`, your project will have:

```
config/
  project.json          — Business identity, market, audience, tone, CTA, sources
  content_pillars.json  — Content strategy with 3-4 themed pillars
  seo_keywords.json     — Keyword targets by priority and intent
  quality_checklist.json — Quality validation standards
  image-generation.json — Image generation backend config
  brands/               — Visual identity assets
```

## Output Structure

All content is organized by date:

```
data/
  research/YYYYMMDD/           — Research findings (JSON)
  briefs/YYYYMMDD/             — Content briefs (JSON)
  drafts/YYYYMMDD/             — Article drafts (Markdown + metadata JSON)
  competitive_analysis/YYYYMMDD/ — Competitor reports (Markdown)
  images/YYYYMMDD/             — Image prompts and generated images
```

## Quality Standards

Articles are validated against a dual-tier checklist:

**Tier 1 (Government content)**: 15 checks, pass score 13/15 (86.7%)
**Tier 2 (Market content)**: 12 checks, pass score 10/12 (83.3%)

Key checks include: data-driven hooks, 3+ statistics with local currency, actionable steps with URLs, FAQ sections, SEO optimization, and professional tone.

## Customization

See `CONNECTORS.md` for information on swapping SerpAPI for a different search provider.

See `references/config-examples/` for a complete example configuration.
