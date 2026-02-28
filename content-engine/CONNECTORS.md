# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. Plugins are tool-agnostic — they describe workflows in terms of categories rather than specific products.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Search API | `~~search api` | SerpAPI | Google Custom Search, Bing Search API |

## Setup

### SerpAPI (included by default)

1. Sign up at [serpapi.com](https://serpapi.com) (free tier: 100 searches/month)
2. Set your API key as an environment variable:
   ```bash
   export SERPAPI_API_KEY=your_key_here
   ```
3. The `/analyze-competitors` command will automatically use SerpAPI for SERP data

### Using a different search API

If you prefer a different search provider, you can update `.mcp.json` in the plugin root to point to your preferred MCP-compatible search server. The `/analyze-competitors` command references `~~search api` and will work with any provider that returns structured search results.
