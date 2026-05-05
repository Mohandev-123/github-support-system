"""FAISS vector store with local file storage."""
import json
import os
from typing import List, Dict, Tuple
import faiss
import numpy as np
from utils.embeddings import EmbeddingsManager


class VectorStore:
    """FAISS-based vector store with local metadata."""

    def __init__(self, store_dir: str = "data/embeddings"):
        self.store_dir = store_dir
        os.makedirs(store_dir, exist_ok=True)
        self.index_path = os.path.join(store_dir, "faiss_index")
        self.metadata_path = os.path.join(store_dir, "metadata.json")
        self.embeddings_manager = EmbeddingsManager()
        self.index = None
        self.metadata = []
        self.load_or_create()

    def load_or_create(self):
        """Load existing index or create new one."""
        if os.path.exists(self.index_path) and os.path.exists(self.metadata_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.metadata_path, "r") as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(384)

    def add_documents(self, chunks: List[Dict]) -> None:
        """Add document chunks to vector store."""
        texts = [chunk["text"] for chunk in chunks]
        embeddings = self.embeddings_manager.embed_texts(texts)
        self.index.add(embeddings.astype(np.float32))
        self.metadata.extend(chunks)
        self.save()

    def search(self, query: str, k: int = 5) -> List[Tuple[Dict, float]]:
        """Search for similar documents."""
        query_embedding = self.embeddings_manager.embed_single(query)
        distances, indices = self.index.search(
            np.array([query_embedding]).astype(np.float32), k
        )
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(self.metadata):
                results.append((self.metadata[idx], float(distances[0][i])))
        return results

    def save(self) -> None:
        """Save index and metadata to disk."""
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "w") as f:
            json.dump(self.metadata, f)

    def clear(self) -> None:
        """Clear index and metadata."""
        self.index = faiss.IndexFlatL2(384)
        self.metadata = []
        self.save()
