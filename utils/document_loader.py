"""Document loading and preprocessing."""
import os
from pathlib import Path
from typing import List
import markdown
from pypdf import PdfReader


class DocumentLoader:
    """Load documents from various formats."""

    @staticmethod
    def load_markdown(file_path: str) -> str:
        """Load markdown file and convert to text."""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    @staticmethod
    def load_pdf(file_path: str) -> str:
        """Extract text from PDF."""
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text

    @staticmethod
    def load_from_directory(directory: str) -> List[tuple[str, str]]:
        """Load all docs from directory. Returns list of (filename, content)."""
        docs = []
        for file_path in Path(directory).rglob("*"):
            if file_path.suffix in [".md", ".txt"]:
                try:
                    content = DocumentLoader.load_markdown(str(file_path))
                    docs.append((file_path.name, content))
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
            elif file_path.suffix == ".pdf":
                try:
                    content = DocumentLoader.load_pdf(str(file_path))
                    docs.append((file_path.name, content))
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
        return docs
