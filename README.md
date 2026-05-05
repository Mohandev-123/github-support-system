# GitHub Support System - Multi-Agent RAG

A Python-based multi-agent system with RAG (Retrieval-Augmented Generation) for answering GitHub documentation questions.

## Setup

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

1. Copy `.env.example` to `.env`
2. Add your Anthropic API key to `.env`

```bash
cp .env.example .env
```

Edit `.env`:
```
API_KEY=your-anthropic-api-key
```

## Usage

### Option 1: Download from GitHub Docs URLs

Edit `docs_config.json` with your documentation links:

```json
{
  "github_docs_urls": [
    "https://docs.github.com/en/rest/...",
    "https://docs.github.com/en/guides/..."
  ]
}
```

Download and ingest:
```bash
python download_docs.py
```

Or download specific URLs directly:
```bash
python main.py download https://docs.github.com/en/rest/... https://docs.github.com/en/guides/...
```

### Option 2: Ingest Local Documentation

Add documentation files to `data/docs/` (markdown, txt, or PDF).

Ingest them:
```bash
python main.py ingest data/docs
```

### Query Your Documentation

Start interactive Q&A:
```bash
python main.py
```

Example:
```
Ask a question: How do I authenticate with GitHub API?
Ask a question: What webhook events are available?
Ask a question: quit
```

## Project Structure

```
.
├── agents/              # Agent implementations
│   ├── base.py         # Base Agent class
│   └── github_support.py # GitHub support RAG agent
├── utils/              # Utility modules
│   ├── rag_system.py   # RAG system core
│   ├── vector_store.py # FAISS vector store
│   ├── embeddings.py   # Embedding generation
│   ├── text_chunker.py # Document chunking
│   ├── document_loader.py # Document loading
│   ├── url_downloader.py # Download from URLs
│   └── config.py       # Configuration
├── data/
│   ├── docs/           # GitHub documentation (auto-downloaded)
│   └── embeddings/     # FAISS indices (auto-generated)
├── main.py             # Entry point
├── download_docs.py    # Helper to download from config
├── docs_config.json    # URL configuration
└── requirements.txt    # Dependencies
```

## RAG Pipeline

1. **Document Loading** - Load markdown/PDF docs from `data/docs/`
2. **Chunking** - Split documents into 1000-character chunks with overlap
3. **Embeddings** - Convert chunks to embeddings using SentenceTransformers
4. **Vector Store** - Store in local FAISS index with JSON metadata
5. **Query** - Find relevant chunks for user questions
6. **LLM Generation** - Use Claude to generate answers from context

## Technologies

- **RAG**: FAISS (local vector store)
- **Embeddings**: SentenceTransformers (all-MiniLM-L6-v2)
- **LLM**: Claude (Anthropic API)
- **Storage**: Local JSON + FAISS (no database)
