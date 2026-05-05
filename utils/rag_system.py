"""RAG system - core retrieval and answering."""
from typing import List
from utils.document_loader import DocumentLoader
from utils.text_chunker import TextChunker
from utils.vector_store import VectorStore


class RAGSystem:
    """Retrieval-Augmented Generation system."""

    def __init__(self, store_dir: str = "data/embeddings"):
        self.vector_store = VectorStore(store_dir)
        self.chunker = TextChunker(chunk_size=1000, overlap=100)
        self.loader = DocumentLoader()

    def ingest_documents(self, doc_directory: str) -> int:
        """Load documents from directory and add to vector store."""
        print(f"Loading documents from {doc_directory}...")
        docs = self.loader.load_from_directory(doc_directory)
        print(f"Loaded {len(docs)} documents")

        print("Chunking documents...")
        chunks = self.chunker.chunk_documents(docs)
        print(f"Created {len(chunks)} chunks")

        print("Creating embeddings and storing...")
        self.vector_store.add_documents(chunks)
        print(f"Stored {len(chunks)} chunks in vector store")
        return len(chunks)

    def query(self, question: str, k: int = 5) -> List[dict]:
        """Search for relevant documents."""
        results = self.vector_store.search(question, k=k)
        return [
            {
                "source": result[0]["source"],
                "text": result[0]["text"],
                "distance": result[1]
            }
            for result in results
        ]

    def get_context(self, question: str, k: int = 5) -> str:
        """Get context from relevant documents."""
        results = self.query(question, k=k)
        context = "\n---\n".join([
            f"Source: {r['source']}\n{r['text']}" for r in results
        ])
        return context
