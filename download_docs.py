"""Helper script to download docs from config file."""
import json
import asyncio
from utils.url_downloader import URLDocumentDownloader
from agents.github_support import GitHubSupportAgent


def download_from_config(config_file: str = "docs_config.json"):
    """Download docs from URLs in config file."""
    with open(config_file, "r") as f:
        config = json.load(f)

    urls = config.get("github_docs_urls", [])
    if not urls:
        print("No URLs found in config file")
        return

    print(f"Downloading {len(urls)} documents from GitHub docs...")
    count = URLDocumentDownloader.download_from_urls(urls, "data/docs")
    print(f"✓ Downloaded {count} documents")

    # Ingest
    print("\nIngesting documents into RAG system...")
    agent = GitHubSupportAgent()
    ingest_count = agent.ingest_docs("data/docs")
    print(f"✓ Ingested {ingest_count} document chunks")


async def test_queries():
    """Test queries after ingestion."""
    agent = GitHubSupportAgent()

    test_queries = [
        "How do I authenticate with GitHub API?",
        "What are the rate limits?",
        "How do I create an issue?",
    ]

    print("\nTesting queries...")
    for question in test_queries:
        print(f"\nQ: {question}")
        answer = await agent.process(question)
        print(f"A: {answer[:300]}...")


if __name__ == "__main__":
    download_from_config()
    asyncio.run(test_queries())
