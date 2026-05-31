# TOOLWISE 🔍
### AI-Powered Developer Tools Research Agent

TOOLWISE is an agentic AI system that automates the research and comparison of developer tools. Give it a query like *"best vector databases for RAG"* and it scrapes the web, extracts relevant tools, analyzes each one, and delivers structured recommendations — pricing, language support, API availability, integrations, and more.

---

## How It Works

TOOLWISE runs a 3-step LangGraph workflow:

```
User Query
    │
    ▼
[1] extract_tools   →  Searches the web for articles, extracts specific tool names via LLM
    │
    ▼
[2] research        →  Scrapes each tool's official site via Firecrawl, runs structured LLM analysis
    │
    ▼
[3] analyze         →  Generates a concise developer recommendation based on all collected data
```

Each step is a node in a LangGraph `StateGraph`, passing a shared `ResearchState` between them.

---

## Example Output

```
$ python main.py "open source observability tools"

🔍 Finding articles about: open source observability tools
Extracted tools: Grafana, Prometheus, OpenTelemetry, Jaeger, Signoz

🔬 Researching specific tools: Grafana, Prometheus, OpenTelemetry, Jaeger

📊 Results for: open source observability tools
============================================================

1. 🏢 Grafana
   🌐 Website: https://grafana.com
   💰 Pricing: Freemium
   📖 Open Source: True
   🛠️  Tech Stack: Go, React, Prometheus, InfluxDB, Elasticsearch
   💻 Language Support: Python, Go, Java, JavaScript
   🔌 API: ✅ Available
   🔗 Integrations: Prometheus, Loki, AWS CloudWatch, Datadog
   📝 Description: Open-source analytics and monitoring platform for visualizing metrics.

...

Developer Recommendations:
----------------------------------------
Grafana + Prometheus is the industry-standard stack for open source observability...
```

---

## Setup

### Prerequisites
- Python 3.11+
- A [Firecrawl API key](https://firecrawl.dev)
- An [OpenAI API key](https://platform.openai.com)

### Installation

**Using uv (recommended):**
```bash
git clone https://github.com/KenKaneki3/TOOLWISE.git
cd TOOLWISE
uv sync
```

**Using pip:**
```bash
git clone https://github.com/KenKaneki3/TOOLWISE.git
cd TOOLWISE
pip install -r requirements.txt
```

### Environment Variables

Copy the example env file and fill in your keys:
```bash
cp .env.example .env
```

```env
FIRECRAWL_API_KEY=your_firecrawl_key_here
OPENAI_API_KEY=your_openai_key_here
```

---

## Usage

**Interactive mode** (loops until you type `exit`):
```bash
python main.py
```

**Single query mode:**
```bash
python main.py "best CI/CD tools for small teams"
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Workflow orchestration | LangGraph |
| LLM | GPT-4o-mini via LangChain |
| Web scraping | Firecrawl |
| Structured outputs | Pydantic + LangChain `.with_structured_output()` |
| Package manager | uv |

---

## Project Structure

```
TOOLWISE/
├── main.py              # CLI entry point (interactive + single query modes)
├── src/
│   ├── workflow.py      # LangGraph StateGraph — 3-node agentic pipeline
│   ├── models.py        # Pydantic models: ResearchState, CompanyInfo, CompanyAnalysis
│   ├── prompts.py       # All LLM prompt templates
│   └── firecrawl.py     # Firecrawl API wrapper
├── .env.example
└── pyproject.toml
```

---

## Known Limitations

- Results quality depends on Firecrawl's scraping success for a given URL
- GPT-4o-mini is used for cost efficiency; swap to GPT-4o in `workflow.py` for higher accuracy
- Rate limits on both APIs may slow down queries with many tools

---

## License

MIT
