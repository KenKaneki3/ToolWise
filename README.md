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
$ Developer Tools Research Agent

🔍 Developer Tools Query: best vector databases for RAG
🔍 Finding articles about: best vector databases for RAG
Extracted tools: pgvector, Pinecone, Qdrant, Weaviate, Milvus
🔬 Researching specific tools: pgvector, Pinecone, Qdrant, Weaviate
Generating recommendations

📊 Results for: best vector databases for RAG
============================================================

1. 🏢 pgvector
   🌐 Website: https://elest.io/open-source/pgvector/resources/plans-and-pricing
   💰 Pricing: Paid
   📖 Open Source: True
   🛠️  Tech Stack: PostgreSQL, pgvector
   🔗 Integrations: AWS, Digital Ocean, VULTR, Linode
   📝 Description: pgvector is an open-source extension for PostgreSQL that enables efficient storage and querying of vector embeddings, making it ideal for machine learning applications.


2. 🏢 Pinecone
   🌐 Website: https://www.pinecone.io/pricing/
   💰 Pricing: Freemium
   📖 Open Source: False
   🛠️  Tech Stack: Pinecone Database, Inference, Assistant, Dense Indexes, Sparse Indexes
   💻 Language Support: Python
   🔌 API: ✅ Available
   🔗 Integrations: AWS, Google Cloud Platform, Microsoft Azure, Prometheus
   📝 Description: Pinecone is a fully managed vector database designed for building and scaling AI applications effortlessly.


3. 🏢 Qdrant
   🌐 Website: https://qdrant.tech/pricing/
   💰 Pricing: Freemium
   📖 Open Source: None
   🛠️  Tech Stack: API, Terraform, Pulumi, CLI, AWS
   🔌 API: ✅ Available
   🔗 Integrations: AWS, Azure, GCP, Terraform
   📝 Description: Qdrant is a fully managed vector search engine that enables developers to build and scale applications with efficient data retrieval capabilities.


4. 🏢 Weaviate
   🌐 Website: https://weaviate.io/pricing
   💰 Pricing: Freemium
   📖 Open Source: None
   🛠️  Tech Stack: AI Database, Hybrid Search, Dynamic Index, Compression, Multi-tenancy
   💻 Language Support: Python, JavaScript, Go
   🔌 API: ✅ Available
   🔗 Integrations: AWS, GCP, Azure, Metrics Monitoring
   📝 Description: Weaviate is a fully managed AI database that enables developers to build and scale AI applications with features like hybrid search and dynamic indexing.

Developer Recommendations: 
----------------------------------------
For a robust RAG implementation, **Pinecone** is the best choice due to its fully managed service and seamless scaling capabilities. It offers a freemium pricing model, making it accessible for initial projects while allowing for growth. Its main technical advantage is the ease of integration with major cloud providers and its optimized performance for AI applications.

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
