# Lassy LLC Hyper Agents

**7 Hyper AI Agents for an Empire | Built by Roger**

> "For Poor People, By Poor People — AI agents that help anyone build a business."

## What Is This?

Lassy LLC Hyper Agents is a team of 7 AI agents that work together to run an online store. Each agent has a specific job. Together, they handle product research, listing writing, inventory, SEO, video, social media, and customer support.

Roger built this for regular people — his wife, Milo, and millions below the poverty line — so anyone can build a business with AI, not just big companies with money to burn.

## The 7 Agents

| Agent | Job | File |
|-------|-----|------|
| **Scout** | Product research — finds trending products, checks CJ dropshipping | `agents/scout.py` |
| **Scribe** | Listing writer — writes product titles, descriptions | `agents/scribe.py` |
| **Ledger** | Inventory auditor — checks stock, flags zero-inventory | `agents/ledger.py` |
| **Beacon** | SEO optimizer — optimizes listings for search | `agents/beacon.py` |
| **Video** | Video content creator — ties into AI-Video system | `agents/video.py` |
| **Social** | Social media poster — Facebook, Instagram posts | `agents/social.py` |
| **Support** | Customer support — answers questions, handles orders | `agents/support.py` |

## Quick Start

```bash
# Install
pip install -r requirements.txt

# Copy env template (optional — works in demo mode without keys)
cp .env.example .env

# Run one agent
python main.py --agent scout --topic "Halloween decorations"

# Run all agents on a product
python main.py --product "Pumpkin LED Lantern" --all

# Run the full pipeline (research → write → SEO → social)
python main.py --pipeline --topic "Christmas gifts"
```

## Demo Mode

Works WITHOUT any API keys. Agents use built-in templates and mock data to show you how it works. Perfect for testing and learning.

With API keys (optional):
- `OPENAI_API_KEY` — AI-powered writing (Scout, Scribe, Beacon)
- `CJ_API_KEY` — Real CJ product data (Scout, Ledger)
- `SHOPIFY_ACCESS_TOKEN` — Real store inventory (Ledger)

## How Agents Work Together

```
Scout finds a product → Scribe writes the listing → Beacon optimizes SEO
    → Video creates content → Social posts it → Ledger tracks inventory
    → Support answers customer questions
```

The `orchestrator.py` coordinates all 7 agents in a pipeline.

## Each Agent

### 1. Scout — Product Research
- Searches trending products by category/season
- Checks CJ Dropshipping for availability, price, stock
- Calculates profit margin (retail − landed cost)
- Filters by Roger's rules: ≥$5 profit, no lithium, no liquids, no ingestibles
- Output: List of vetted product candidates

### 2. Scribe — Listing Writer
- Writes product titles (SEO-friendly, under 70 chars)
- Writes descriptions (benefits-first, honest delivery times)
- Writes bullet points (features, specs, what's included)
- Includes price, delivery estimate, call-to-action

### 3. Ledger — Inventory Auditor
- Checks Shopify store inventory
- Flags zero-inventory live products (restock or unpublish?)
- Flags drafts with inventory (launch candidates)
- Tracks sales, orders, revenue
- Generates audit reports

### 4. Beacon — SEO Optimizer
- Researches keywords for a product
- Optimizes title, description, tags for search
- Suggests category and collection placement
- Scores listing SEO (0-100)

### 5. Video — Video Content Creator
- Generates video scripts for products
- Creates video ideas (unboxing, demo, review)
- Ties into AI-Video system (github.com/Rogersyfreeman1/AI-Video)
- Suggests thumbnails, titles, tags

### 6. Social — Social Media Poster
- Drafts Facebook posts (with hashtags, CTA, link)
- Drafts Instagram captions (carousel, story, reel)
- Creates post schedules (best times to post)
- Tracks engagement (likes, comments, shares)

### 7. Support — Customer Support
- Answers common questions (shipping, returns, product info)
- Handles order status inquiries
- Drafts support replies (friendly, helpful tone)
- Escalates complex issues to human

## File Structure

```
lassy-llc-hyper-agents/
├── README.md
├── main.py              # CLI entry point
├── config.py            # Settings, API keys
├── orchestrator.py      # Coordinates all 7 agents
├── requirements.txt
├── .env.example
├── agents/
│   ├── __init__.py
│   ├── scout.py
│   ├── scribe.py
│   ├── ledger.py
│   ├── beacon.py
│   ├── video.py
│   ├── social.py
│   └── support.py
└── output/              # Generated files go here
```

## Example: Full Pipeline

```bash
python main.py --pipeline --topic "Halloween decorations"
```

Output:
1. **Scout** finds 5 Halloween products with profit ≥$5
2. **Scribe** writes listings for each
3. **Beacon** optimizes SEO for each listing
4. **Video** generates video scripts
5. **Social** drafts Facebook + Instagram posts
6. **Ledger** checks if products are already in store
7. **Support** prepares FAQ answers

All output saved to `output/` folder.

## Built By

**Roger Freeman** — CEO & Founder, Lassy LLC
Building an economy for poor people.

## License

MIT — Free for anyone to use, especially people building their way out of poverty.
