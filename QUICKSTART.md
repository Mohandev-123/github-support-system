# GitHub Support System - Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Activate Virtual Environment
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
venv\Scripts\activate.bat

# macOS/Linux
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- FAISS (vector store)
- SentenceTransformers (embeddings)
- OpenAI SDK (for OpenRouter support)
- Anthropic SDK (optional)
- BeautifulSoup4 (HTML parsing)
- And more...

### Step 3: Ingest GitHub Documentation Corpus

The system comes pre-configured with 24 GitHub documentation URLs covering:
- GitHub Plans & Billing
- REST API Documentation
- Authentication (PAT, SAML)
- Organizations & Enterprise

**Download & ingest everything:**
```bash
python ingest_corpus.py
```

---

## 🔑 API Configuration

### Option 1: OpenRouter (Recommended)

Edit `.env`:
```bash
API_PROVIDER=openrouter
OPENROUTER_API_KEY=your-openrouter-api-key
MODEL=claude-opus-4-7
```

**Why OpenRouter?**
- ✅ Single API key works with multiple models
- ✅ Better pricing and rate limits
- ✅ Easy model switching
- ✅ Supports Claude, GPT-4, Mistral, etc.

### Option 2: Direct Anthropic API

Edit `.env`:
```bash
API_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-anthropic-api-key
MODEL=claude-opus-4-7
```

---

Once ingestion is complete:

```bash
python main.py
```

### Example Queries:

**Billing:**
- "What are GitHub's pricing plans?"
- "How do I upgrade my plan?"
- "What's included in GitHub Pro?"

**REST API:**
- "How do I authenticate with the REST API?"
- "What are the rate limits?"
- "How do I create an issue via API?"

**Authentication:**
- "What is a personal access token?"
- "How do I set up SAML SSO?"
- "What scopes should I request?"

**Type `quit` to exit**

---

## 📊 System Architecture

```
User Question
     ↓
[Vector Search] → Find similar docs in FAISS
     ↓
[Context Retrieval] → Get top 5 chunks
     ↓
[Claude LLM] → Generate answer from context
     ↓
Answer to User
```

**Storage:** Local only (no database needed)
- FAISS index: `data/embeddings/faiss_index`
- Metadata: `data/embeddings/metadata.json`
- Downloaded docs: `data/docs/*.md`

---

## 🔧 Advanced Usage

### Custom Documentation URLs

Edit `docs_config.json` to add your own URLs:

```json
{
  "github_docs_urls": [
    "https://docs.github.com/en/...",
    "https://your-docs.com/page",
    "...more URLs"
  ]
}
```

Then run:
```bash
python download_docs.py
```

### Download & Ingest Specific URLs

```bash
python main.py download https://docs.github.com/en/rest/... https://docs.github.com/en/...
```

### Ingest Local Files

Place markdown/PDF files in `data/docs/` then:
```bash
python main.py ingest data/docs
```

---

## 🐛 Troubleshooting

**Q: "API key not found"**
- A: Create `.env` and add: `API_KEY=your-anthropic-api-key`

**Q: "Slow ingestion"**
- A: This is normal (2-5 min for 24 docs). Downloads, converts HTML, generates embeddings.

**Q: "Connection errors downloading docs"**
- A: Check internet connection. Some URLs may be temporarily unavailable. Retry.

**Q: "Low quality answers"**
- A: Add more relevant documentation. Quality improves with corpus size.

---

## 📈 Performance

- **Ingestion:** ~2-5 minutes for 24 docs
- **Query:** ~1-2 seconds per question
- **Accuracy:** Based on documentation relevance
- **Storage:** ~500MB-1GB for full corpus

---

## ✅ What's Ready

- ✅ Phase 1: RAG System (Local vector store, no SQL)
- ✅ Phase 1: Document loading (URLs, markdown, PDF)
- ✅ Phase 1: Query system with Claude
- 🔜 Phase 2: Multi-agent collaboration
- 🔜 Phase 3: Context switching between agents
