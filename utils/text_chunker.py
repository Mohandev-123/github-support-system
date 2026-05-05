"""Text chunking and preprocessing."""
from typing import List


class TextChunker:
    """Split documents into chunks for embedding."""

    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str) -> List[str]:
        """Split text into overlapping chunks."""
        chunks = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk.strip())
            start += self.chunk_size - self.overlap
        return chunks

    def chunk_documents(self, docs: List[tuple[str, str]]) -> List[dict]:
        """Convert documents to chunks with metadata."""
        chunks = []
        for filename, content in docs:
            text_chunks = self.chunk_text(content)
            for i, chunk in enumerate(text_chunks):
                chunks.append({
                    "source": filename,
                    "chunk_id": i,
                    "text": chunk
                })
        return chunks
