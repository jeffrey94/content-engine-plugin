# Auto-Selection Matrix

## Purpose

Maps article content signals to recommended style + mood combinations. Used in Step 3 of the workflow when presenting recommendations to the user.

## Signal Priority

When multiple signals conflict, use this priority order:

1. **Content pillar** (from article YAML frontmatter) -- highest priority
2. **Title keywords** (scanned from article title)
3. **Body keywords** (scanned from first 500 words)
4. **Hook type** (from article frontmatter if available) -- lowest priority

## Content Pillar Matrix

| Content Pillar | Primary Style | Secondary Style | Mood |
|---|---|---|---|
| Policy & Compliance | corporate-modern | minimal-line | professional |
| Funding & Financing | data-visual | corporate-modern | professional |
| Industry Opportunities | isometric | bold-graphic | energetic |
| Practical Guides | hand-drawn | flat-vector | warm |

## Title & Body Keyword Signals

| Keywords | Recommended Style | Mood |
|---|---|---|
| tax, filing, compliance, deadline, regulation, LHDN, SSM | corporate-modern | professional |
| RM, financing, loan, cash flow, invoice, payment, capital | data-visual | professional |
| data center, semiconductor, supply chain, manufacturing, infrastructure | isometric | energetic |
| guide, how to, how-to, comparison, vs, step-by-step, checklist | flat-vector or hand-drawn | warm |
| Malaysia 2026, tourism, Visit Malaysia, cultural, heritage | cultural-motif | warm |
| urgent, deadline, breaking, new, must, critical, mandatory | bold-graphic | energetic |
| growth, opportunity, export, market, trend, expansion | bold-graphic | energetic |
| success story, case study, community, partnership | watercolor | warm |
| premium, executive, leadership, strategy, board | minimal-line | professional |
| statistics, data, report, survey, index, benchmark | data-visual | professional |
| technology, digital, automation, AI, software, platform | isometric | professional |
| halal, certification, export, MATRADE, JAKIM | cultural-motif | professional |

## Hook Type Signals

| Hook Type | Style Tendency | Mood |
|---|---|---|
| curiosity | hand-drawn or watercolor | warm |
| urgency | bold-graphic or corporate-modern | energetic |
| data-driven | data-visual or flat-vector | professional |
| storytelling | watercolor or hand-drawn | warm |
| contrarian | bold-graphic | energetic |

## Recommendation Logic

1. Check `content_pillar` in frontmatter -> get Primary Style + Mood from Content Pillar Matrix
2. Scan title for keyword matches -> if match found and conflicts with pillar recommendation, note both as options
3. Scan first 500 words for keyword density -> reinforce or adjust
4. Check hook type if available -> use as tiebreaker only
5. Present to user: "Recommended: {primary_style} + {mood} because {reasoning}. Alternative: {secondary_style}."

## Example Recommendations

**Article:** "Complete Guide to E-Invoicing Phase 2 for Malaysian SMEs"
- Pillar: Policy & Compliance -> corporate-modern + professional
- Keywords: "guide" (hand-drawn/warm), "e-invoicing" (compliance/professional)
- Result: **corporate-modern + professional** (pillar wins, "guide" keyword noted as alternative)
- Presented as: "Recommended: corporate-modern + professional (compliance content). Alternative: hand-drawn + warm (guide-style article)."

**Article:** "5 Government Financing Programs Most Malaysian SMEs Don't Know About"
- Pillar: Funding & Financing -> data-visual + professional
- Keywords: "government" (compliance), "financing" (data-visual), "don't know" (curiosity hook)
- Result: **data-visual + professional** (pillar aligns with keywords)

**Article:** "How Malaysian Data Centers Are Attracting RM30 Billion in Foreign Investment"
- Pillar: Industry Opportunities -> isometric + energetic
- Keywords: "data center" (isometric), "RM30 billion" (data-visual), "investment" (energetic)
- Result: **isometric + energetic** (perfect alignment)
