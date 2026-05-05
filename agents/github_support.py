"""GitHub Support Agent using RAG."""
import asyncio
from agents.base import Agent
from utils.rag_system import RAGSystem
from utils.llm_client import LLMClient, LLMConfig


class GitHubSupportAgent(Agent):
    """Agent that answers GitHub questions using RAG."""

    def __init__(self, name: str = "GitHub Support", rag_dir: str = "data/embeddings"):
        super().__init__(name, role="GitHub Documentation Expert")
        self.rag = RAGSystem(rag_dir)
        self.config = LLMConfig()
        self.llm = LLMClient(self.config)
        self.conversation_history = []

    async def process(self, question: str) -> str:
        """Answer a GitHub question using RAG."""
        # Get context from RAG
        context = self.rag.get_context(question, k=5)

        # Build prompt with context
        system_prompt = """You are a GitHub support expert. Answer the following question using the provided documentation context.

Provide clear, concise, and helpful answers. If the context doesn't contain relevant information, say so."""

        prompt = f"""Question: {question}

Context from GitHub Documentation:
{context}

Please provide a helpful answer based on the documentation."""

        # Call LLM
        messages = [
            {"role": "user", "content": prompt}
        ]

        answer = self.llm.generate(messages)

        self.conversation_history.append({
            "role": "user",
            "content": question
        })
        self.conversation_history.append({
            "role": "assistant",
            "content": answer
        })

        return answer

    async def collaborate(self, other_agent: Agent, message: str) -> str:
        """Collaborate with another agent."""
        return f"{self.name} received message from {other_agent.name}: {message}"

    def ingest_docs(self, doc_directory: str) -> int:
        """Ingest GitHub documentation."""
        return self.rag.ingest_documents(doc_directory)

