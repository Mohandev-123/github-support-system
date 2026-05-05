"""Download and fetch documents from URLs."""
import os
from typing import List, Set
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


class URLDocumentDownloader:
    """Download documents from URLs."""

    @staticmethod
    def fetch_url(url: str) -> str:
        """Fetch content from URL."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=10, headers=headers)
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
        for script in soup(["script", "style", "nav"]):
            script.decompose()
        text = soup.get_text()
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text

    @staticmethod
    def extract_links(html: str, base_url: str) -> List[str]:
        """Extract all links from HTML that belong to the same domain."""
        soup = BeautifulSoup(html, "html.parser")
        links = []
        base_domain = urlparse(base_url).netloc
        
        for link in soup.find_all("a", href=True):
            href = link["href"]
            full_url = urljoin(base_url, href)
            # Remove fragments
            full_url = full_url.split("#")[0]
            
            # Only include links from same domain and /en/rest path
            if urlparse(full_url).netloc == base_domain and "/en/rest" in full_url:
                links.append(full_url)
        
        return links

    @staticmethod
    def crawl_github_rest_api(start_url: str = "https://docs.github.com/en/rest", 
                              output_dir: str = "data/docs", max_pages: int = 100) -> int:
        """Crawl GitHub REST API docs starting from a URL."""
        os.makedirs(output_dir, exist_ok=True)
        visited: Set[str] = set()
        to_visit: List[str] = [start_url]
        saved_count = 0
        
        print(f"Starting crawl from: {start_url}")
        print(f"Max pages to crawl: {max_pages}\n")
        
        while to_visit and len(visited) < max_pages:
            url = to_visit.pop(0)
            
            if url in visited:
                continue
                
            visited.add(url)
            print(f"Crawling ({len(visited)}/{max_pages}): {url}")
            
            content = URLDocumentDownloader.fetch_url(url)
            if not content:
                continue
            
            # Convert HTML to text
            text = URLDocumentDownloader.html_to_text(content)
            
            # Extract links for further crawling
            links = URLDocumentDownloader.extract_links(content, url)
            for link in links:
                if link not in visited and link not in to_visit:
                    to_visit.append(link)
            
            # Save document
            filename = f"doc_{len(visited)}.md"
            filepath = os.path.join(output_dir, filename)
            
            try:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(f"# Source: {url}\n\n")
                    f.write(text)
                print(f"  ✓ Saved to {filename}")
                saved_count += 1
            except Exception as e:
                print(f"  ✗ Error saving: {e}")
        
        print(f"\n✓ Crawl complete! Visited {len(visited)} pages, saved {saved_count} documents")
        return saved_count

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
