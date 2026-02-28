---
description: Set up or reconfigure your brand and content strategy
allowed-tools: Read, Write, Edit, Glob, Bash(mkdir:*, date:*, ls:*, cp:*)
---

# Brand Setup

Guide the user through configuring the content engine for their business. This creates or updates the config files that power all other commands.

## Detect State

1. Read `config/project.json`.
2. Check:
   - If `project_id` is `"UNCONFIGURED"` or `setup_complete` is `false` → **New setup** (run all steps)
   - If `setup_complete` is `true` → **Reconfiguration** (ask what to change, update only those sections)

If `config/project.json` doesn't exist, create the directory structure first:
```
config/
  project.json
  content_pillars.json
  seo_keywords.json
  quality_checklist.json
  brands/
    _template.json
    _active.json
```

Copy templates from `${CLAUDE_PLUGIN_ROOT}/references/config-templates/`.

## Step 1: Business Identity

Ask the user about their business. Use AskUserQuestion where helpful:

- **Business name** and short name
- **Description**: what the business does (1-2 sentences)
- **Website** and blog URL
- **Services**: what they offer (list 3-5)
- **Value proposition**: what makes them unique

Then ask about their **market**:
- Country and currency
- Language
- Local search modifiers (cities, regions)
- Government domains (e.g., ".gov.my")
- Trusted local news domains

Then ask about their **audience**:
- Who they're writing for (label like "Malaysian SMEs" or "Fitness enthusiasts")
- Revenue range or demographic profile
- Target industries (3-5 specific ones)
- Top pain points (3-5)
- Decision-maker job titles

Write all answers to `config/project.json` → `business`, `market`, `audience` sections.

## Step 2: Content Strategy

Ask about content approach:

- **Business objective**: what they want content to achieve (e.g., "Increase organic traffic by 30% in 6 months")
- **Content split**: percentage of government/policy vs market/industry content (default 50/50)
- **Articles per month**: target volume (default 2-4)
- **Word count preferences**: confirm defaults (Tier 1: 1,200-1,800, Tier 2: 1,000-1,500)

Then define **3-4 content pillars**. For each pillar:
- Name and description
- Content split (government vs market %)
- Target audience within the pillar
- 5-10 example topics
- 5-10 target keywords
- Typical CTA angle connecting pillar to brand

Write to `config/content_pillars.json`.

If the user is unsure, suggest pillars based on their business type and audience.

## Step 3: SEO Keywords

Ask for or help generate:

- **Primary keywords** (5-10): high-priority terms for the business with estimated competition
- **Secondary keywords** (10-20): supporting terms
- **Long-tail keywords**: patterns like "how to [action] in [market]"
- **Competitor keywords**: terms their competitors rank for
- **Local modifiers**: country, city, region terms
- **Industry modifiers**: sector-specific terms
- **Intent keywords**: informational (what is, how to), commercial (best, top, vs), transactional (apply, get)

Write to `config/seo_keywords.json`.

If the user says "you suggest", use WebSearch to research their industry + market and propose keywords.

## Step 4: Tone & CTA

Confirm or customize:

- **Voice**: default "Expert but accessible"
- **Style**: default "Friendly but professional"
- **Approach**: default "Helpful, not salesy"
- **Writing rules**: use local currency, reference local agencies, active voice, direct address, short paragraphs
- **CTA style**: default "soft"
- **CTA placement**: default "end of article"
- **CTA angles**: 2-3 typical ways to connect content to the brand

Write to `config/project.json` → `tone`, `cta` sections.

## Step 5: Regulatory & Sources (if applicable)

If the business involves government-regulated content:
- **Agencies**: name, full name, URL, focus area (3-5)
- **Known programs**: government programs relevant to the audience
- **Compliance topics**: regulatory areas to cover

For all businesses:
- **News sources**: front pages, business sections (3-5)
- **Macro sources**: economic data providers
- **Industry associations**: relevant to their sector
- **Search keywords** by category: base, financing, compliance, industry

Write to `config/project.json` → `regulatory`, `research_sources` sections.

## Step 6: Brand Identity (Optional)

Ask if they want to set up visual identity for image generation:

- **Brand colors**: primary, secondary, accent (hex values)
- **Typography**: heading, body, display fonts
- **Visual descriptors**: 3 words (e.g., "modern, trustworthy, approachable")
- **Avoid**: visual styles to avoid
- **Cultural notes**: any cultural considerations

Copy `config/brands/_template.json` → `config/brands/{brand-slug}.json`, fill in values, update `config/brands/_active.json`.

## Step 7: Finalize

1. Set `project_id` to the brand slug in `config/project.json`
2. Set `setup_complete: true`
3. Create the data directory structure:
   ```
   data/
     research/
     briefs/
     drafts/
     competitive_analysis/
     images/
   ```
4. Present a summary of the configuration
5. Suggest first commands:
   - `/research` to find trending topics
   - `/write [topic]` to write about a known topic
   - `/content-visuals` to generate article images

## Reconfiguration Mode

If the system is already configured, ask what the user wants to change:
- Business details → update `config/project.json` → `business`
- Content pillars → update `config/content_pillars.json`
- SEO keywords → update `config/seo_keywords.json`
- Tone/CTA → update `config/project.json` → `tone`, `cta`
- Sources → update `config/project.json` → `research_sources`
- Brand visuals → update `config/brands/`

Only modify the requested sections, leave everything else unchanged.

## Reference Files

Example configuration available at `${CLAUDE_PLUGIN_ROOT}/references/config-examples/` showing a complete filled-out config for a sample business.
