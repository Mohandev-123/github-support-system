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
        """Answer a GitHub question using RAG - ONLY from documentation."""
        # Get context from RAG
        context = self.rag.get_context(question, k=5)

        # Build strict prompt - NO GUESSING
        system_prompt = """You are a GitHub support expert with strict rules:

RULES:
1. ONLY answer using information from the provided documentation context
2. If the documentation does NOT contain relevant information, respond with:
   "I cannot answer this question - the information is not available in the GitHub REST API documentation."
3. Never guess, assume, or add information not in the context
4. Always cite which documentation section your answer comes from
5. If the question is unclear or outside GitHub REST API scope, say so

Be accurate. Be cautious. Answer only from what you know from the docs."""

        prompt = f"""Question: {question}

Documentation Context:
{context}

IMPORTANT: Only use the documentation provided above. If it doesn't have the answer, say so clearly."""

        # Call LLM
        messages = [
            {"role": "system", "content": system_prompt},
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

