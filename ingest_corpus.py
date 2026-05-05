"""Download GitHub REST API docs with web crawling."""
import json
import time
from utils.url_downloader import URLDocumentDownloader
from agents.github_support import GitHubSupportAgent


def download_corpus():
    """Download full GitHub REST API documentation via web crawling."""
    print(f"📚 GitHub Support System - REST API Doc Crawling")
    print("=" * 60)

    start_time = time.time()

    # Crawl GitHub REST API docs
    print("🕷️  Crawling GitHub REST API documentation...")
    print("    Source: https://docs.github.com/en/rest\n")
    downloaded = URLDocumentDownloader.crawl_github_rest_api(
        start_url="https://docs.github.com/en/rest",
        output_dir="data/docs",
        max_pages=150
    )
    print(f"✓ Downloaded: {downloaded} documents\n")

    # Ingest
    print("⚙️  Processing and ingesting into RAG system...")
    agent = GitHubSupportAgent()
    ingested = agent.ingest_docs("data/docs")
    print(f"✓ Ingested: {ingested} document chunks\n")

    elapsed = time.time() - start_time
    print(f"⏱️  Time elapsed: {elapsed:.1f}s")
    print("\n✅ Knowledge base ready! Run 'python main.py' to start querying.\n")

    return downloaded, ingested


if __name__ == "__main__":
    try:
        download_corpus()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
