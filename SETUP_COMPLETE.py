"""
🚀 GitHub Support System - Ready to Go!

✅ What's configured:
- API Provider: OpenRouter
- Model: Mistral 7B (best free option)
- Temperature: 0.3 (precise, good for factual docs)
- Max Tokens: 2048
- Storage: Local FAISS (no database)

📋 Next Steps:

1. INSTALL DEPENDENCIES (first time only):
   pip install -r requirements.txt

2. TEST CONNECTION:
   python test_connection.py

3. INGEST GITHUB DOCS (takes 3-5 min):
   python ingest_corpus.py

4. START QUERYING:
   python main.py

═══════════════════════════════════════════════

🎯 Why Mistral 7B?
- ✅ FREE on OpenRouter
- ✅ Fast inference (1-2s per query)
- ✅ Good instruction following (great for RAG)
- ✅ Low latency
- ✅ Works well with formatted context

📊 Expected Performance:
- Query response: 1-2 seconds
- Accuracy: High (based on GitHub docs)
- Cost: FREE (Mistral 7B)

💡 Can upgrade model anytime:
Edit .env and change MODEL= to:
- gpt-3.5-turbo (faster, better quality)
- claude-opus (slower, best quality)
- gpt-4 (premium)

═══════════════════════════════════════════════
"""
print(__doc__)
