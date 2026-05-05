"""Download and fetch documents from URLs."""
import os
from typing import List
import requests
from bs4 import BeautifulSoup


class URLDocumentDownloader:
    """Download documents from URLs."""

    @staticmethod
    def fetch_url(url: str) -> str:
        """Fetch content from URL."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return ""

    @staticmethod
    def html_to_text(html: str) -> str:
        """Convert HTML to plain text."""
        soup = BeautifulSoup(html, "html.parser")
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text()
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    @staticmethod
    def download_from_urls(urls: List[str], output_dir: str = "data/docs") -> int:
        """Download docs from list of URLs and save as markdown."""
        os.makedirs(output_dir, exist_ok=True)
        saved_count = 0

        for i, url in enumerate(urls):
            print(f"Downloading {i+1}/{len(urls)}: {url}")
            content = URLDocumentDownloader.fetch_url(url)

            if not content:
                continue

            # Convert HTML to text if needed
            if content.strip().startswith("<"):
                content = URLDocumentDownloader.html_to_text(content)

            # Generate filename from URL
            filename = f"doc_{i+1}.md"
            filepath = os.path.join(output_dir, filename)

            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# Source: {url}\n\n")
                    f.write(content)
                print(f"  ✓ Saved to {filename}")
                saved_count += 1
            except Exception as e:
                print(f"  ✗ Error saving: {e}")

        return saved_count
