"""Embeddings using sentence-transformers."""
import json
import os
import pickle
from typing import List
import numpy as np
from sentence_transformers import SentenceTransformer


class EmbeddingsManager:
    """Create and manage embeddings."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.model_name = model_name

    def embed_texts(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for list of texts."""
        embeddings = self.model.encode(texts, show_progress_bar=False)
        return embeddings

    def embed_single(self, text: str) -> np.ndarray:
        """Generate embedding for single text."""
        return self.model.encode([text])[0]
