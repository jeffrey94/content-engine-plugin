---
name: content-style
description: >
  Apply brand tone, voice, and formatting standards to blog content. Use when
  the user asks to "write an article", "check content style", "apply brand voice",
  "format blog content", or needs guidance on article structure, hook writing,
  TL;DR formatting, FAQ sections, or CTA placement.
version: 0.2.0
---

# Content Style Guide

Standards for tone, voice, and structure across all blog content. Load business context from `config/project.json` in the user's project folder.

## Tone & Voice

- **Voice**: Expert but accessible
- **Style**: Friendly but professional
- **Approach**: Helpful, not salesy
- **Context**: Always local — use the market's currency, agencies, and regulations from `config/project.json`

## Article Structure

Every article follows this skeleton:

1. **Hook** — specific fact with local currency value, percentage, or surprising data point (100-150 words)
2. **TL;DR** — 3-5 bullet points, each with a bold label (Key fact / Action / Deadline / Benefit / Warning), specific data, one sentence each (50-75 words)
3. **Body** — 3-5 sections with H2 headers. Short paragraphs (2-3 sentences max). Statistics, data, examples throughout (600-900 words)
4. **Actionable Steps** — numbered list with specific URLs, registration processes, deadlines, required documents (150-250 words)
5. **FAQ** — 5-7 questions in exact search format ("What is…", "How do I…", "When is…", "How much…"). Direct answers, 2-4 sentences each (200-300 words)
6. **Conclusion + CTA** — 2-3 key takeaways, soft CTA connecting topic to brand (100-150 words)

## Hook Requirements

- Opens with specific local currency value, percentage, or data point
- Relevant to the target audience defined in `config/project.json`
- Creates curiosity or urgency
- Cites a credible, recent source
- Active voice throughout

**Bad**: "Cash flow is important for SMEs."
**Good**: "[Target audience] wait an average of X days for payment, tying up [currency][amount] in working capital [source]."

## TL;DR Format

Place immediately after the hook. Format:

- **Key fact**: [specific data with local currency or percentage]
- **Action**: [what to do, with named program or portal]
- **Deadline**: [specific date if applicable]
- **Benefit**: [quantified outcome]

## Tables

Use tables for:
- Before/after comparisons
- Multi-attribute data (relief types, amounts, deadlines)
- Step-by-step processes with multiple columns

Keep tables simple and mobile-friendly.

## Government Programs

When referencing government programs:
- Use official program names from `config/project.json` → `regulatory`
- Include what the program offers, deadlines, requirements
- Link to official portals

## Actionable Steps

Every article must include concrete next steps:
- Specific URLs to portals or services
- Step-by-step registration or application processes
- Deadlines and timeframes
- Required documents or eligibility criteria
- Contact information where available

## FAQ Section

- 5-7 questions optimized for "People Also Ask" and voice search
- Must include at least: 1× "What…", 1× "How…", 1× "When…" or deadline question, 1× "How much…" or amount question
- Direct answers in active voice, 2-4 sentences each
- Include specific currency values, deadlines, or requirements

## CTA Guidelines

- **Position**: End of article, after actionable steps
- **Style**: Soft, helpful — not salesy
- **Connection**: Natural bridge from article topic to brand offering
- **Length**: 2-4 sentences
- Load CTA angles from `config/project.json` → `cta`

## Formatting

- Markdown with proper heading hierarchy (H1 → H2 → H3)
- Hyperlinks with descriptive anchor text (never "click here")
- Hybrid citation style:
  - First mention: full inline attribution + bracketed letter `[a]`
  - Subsequent mentions: letter only `[a]`
  - References section at end: `[a] Source Name - URL`

## SEO Requirements

- Title ≤ 60 characters, includes primary keyword
- Meta description 150-160 characters with keyword and CTA
- Primary keyword in title, first paragraph, and at least one H2
- Natural keyword distribution throughout
- Proper heading hierarchy

## Word Count

- **Target**: 1,200-1,300 words
- **Range**: 1,000-1,500 words
- Paragraphs: 2-3 sentences max
- Scannable: bullet points, tables, short sections

## Content Pillars

Load from `config/content_pillars.json`. Each pillar defines topics, keywords, and audience focus. Match article content to the appropriate pillar.

## Common Mistakes to Avoid

- Generic openings without data
- Vague claims without statistics
- International examples instead of local ones
- Generic advice applicable to any country
- Aggressive or salesy CTAs
- Keyword stuffing
- Long paragraphs (>3 sentences)
- Passive voice
- Missing TL;DR or FAQ sections
- Data presented in lists instead of tables
