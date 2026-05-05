"""Test script for RAG system."""
import asyncio
from agents.github_support import GitHubSupportAgent


async def test_rag():
    """Test RAG system with sample docs."""
    print("Testing GitHub Support RAG System")
    print("=" * 50)

    # Initialize agent
    agent = GitHubSupportAgent()

    # Ingest docs
    print("\n1. Ingesting sample documentation...")
    count = agent.ingest_docs("data/docs")
    print(f"   ✓ Ingested {count} chunks")

    # Test queries
    test_queries = [
        "How do I authenticate with GitHub API?",
        "What are the rate limits for API requests?",
        "How do I set up webhooks?",
    ]

    print("\n2. Testing queries...\n")
    for question in test_queries:
        print(f"Q: {question}")
        answer = await agent.process(question)
        print(f"A: {answer[:200]}...\n")
        print("-" * 50)

    print("\n✓ RAG system test complete!")


if __name__ == "__main__":
    asyncio.run(test_rag())
