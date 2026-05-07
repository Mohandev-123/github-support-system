"""Main entry point - RAG system demo."""
import asyncio
from agents.github_support import GitHubSupportAgent


async def main():
    """Run GitHub support RAG system."""
    agent = GitHubSupportAgent()
    
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


if __name__ == "__main__":
    asyncio.run(main())
