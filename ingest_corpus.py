"""Download all GitHub docs from corpus seed list with progress tracking."""
import json
import time
from utils.url_downloader import URLDocumentDownloader
from agents.github_support import GitHubSupportAgent


def download_corpus():
    """Download full documentation corpus."""
    with open("docs_config.json", "r") as f:
        config = json.load(f)

    urls = config.get("github_docs_urls", [])
    print(f"📚 GitHub Support System - Document Corpus Ingestion")
    print("=" * 60)
    print(f"Total URLs to download: {len(urls)}\n")

    start_time = time.time()

    # Download
    print("🔽 Downloading documentation...")
    downloaded = URLDocumentDownloader.download_from_urls(urls, "data/docs")
    print(f"✓ Downloaded: {downloaded}/{len(urls)} documents\n")

    # Ingest
    print("⚙️  Processing and ingesting into RAG system...")
    agent = GitHubSupportAgent()
    ingested = agent.ingest_docs("data/docs")
    print(f"✓ Ingested: {ingested} document chunks\n")

    elapsed = time.time() - start_time
    print(f"⏱️  Time elapsed: {elapsed:.1f}s")
    print("\n✅ Corpus ready! Run 'python main.py' to start querying.\n")

    return downloaded, ingested


if __name__ == "__main__":
    try:
        download_corpus()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
