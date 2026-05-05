"""Main entry point - RAG system demo."""
import asyncio
import sys
from agents.github_support import GitHubSupportAgent
from utils.url_downloader import URLDocumentDownloader


async def main():
    """Run GitHub support RAG system."""
    agent = GitHubSupportAgent()

    if len(sys.argv) < 2:
        # Interactive mode
        print("GitHub Support RAG System")
        print("-" * 40)
        while True:
            question = input("Ask a question (or 'quit' to exit): ").strip()
            if question.lower() == "quit":
                break
            if not question:
                continue
            print("\nSearching documentation...")
            answer = await agent.process(question)
            print(f"\nAnswer:\n{answer}\n")
        return

    command = sys.argv[1]

    if command == "ingest":
        # Ingest from local directory
        doc_dir = sys.argv[2] if len(sys.argv) > 2 else "data/docs"
        print(f"Ingesting documents from {doc_dir}...")
        count = agent.ingest_docs(doc_dir)
        print(f"✓ Ingested {count} document chunks")

    elif command == "crawl":
        # Crawl GitHub REST API docs
        # Usage: python main.py crawl [pages]
        # Examples: python main.py crawl 20  (fast, ~30 docs)
        #           python main.py crawl 50  (medium, ~60 docs)
        #           python main.py crawl 100 (thorough, ~120 docs)
        try:
            max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 50
        except ValueError:
            print("Usage: python main.py crawl [max_pages]")
            print("Examples: python main.py crawl 20")
            print("          python main.py crawl 50 (default)")
            print("          python main.py crawl 100")
            return
        
        print(f"Crawling GitHub REST API documentation (max {max_pages} pages)...")
        count = await URLDocumentDownloader.crawl_github_rest_api_async(
            start_url="https://docs.github.com/en/rest",
            output_dir="data/docs",
            max_pages=max_pages
        )
        print(f"✓ Downloaded {count} documents")

        # Auto-ingest after crawl
        print("\nIngesting documents into RAG system...")
        ingest_count = agent.ingest_docs("data/docs")
        print(f"✓ Ingested {ingest_count} document chunks")

    elif command == "download":
        # Download from URLs
        if len(sys.argv) < 3:
            print("Usage: python main.py download <url1> [url2] [url3] ...")
            return
        urls = sys.argv[2:]
        print(f"Downloading {len(urls)} documents...")
        count = URLDocumentDownloader.download_from_urls(urls, "data/docs")
        print(f"✓ Downloaded {count} documents")

        # Auto-ingest after download
        print("\nIngesting documents...")
        ingest_count = agent.ingest_docs("data/docs")
        print(f"✓ Ingested {ingest_count} document chunks")

    else:
        print("Usage:")
        print("  python main.py                          # Interactive mode")
        print("  python main.py ingest <directory>       # Ingest local docs")
        print("  python main.py download <url1> <url2>   # Download and ingest from URLs")


if __name__ == "__main__":
    asyncio.run(main())
