"""Download and fetch documents from URLs."""
import os
import asyncio
from typing import List, Set
import aiohttp
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
    async def fetch_url_async(url: str, session: aiohttp.ClientSession) -> str:
        """Fetch content from URL asynchronously."""
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                return await response.text()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return ""

    @staticmethod
    async def crawl_github_rest_api_async(start_url: str = "https://docs.github.com/en/rest", 
                              output_dir: str = "data/docs", max_pages: int = 50) -> int:
        """Async crawl implementation with concurrent requests."""
        os.makedirs(output_dir, exist_ok=True)
        visited: Set[str] = set()
        to_visit: List[str] = [start_url]
        saved_count = 0
        
        print(f"Starting fast crawl from: {start_url}")
        print(f"Max pages to crawl: {max_pages}\n")
        
        # Use connection pooling for faster requests
        connector = aiohttp.TCPConnector(limit=10, limit_per_host=5)
        async with aiohttp.ClientSession(connector=connector) as session:
            while to_visit and len(visited) < max_pages:
                # Process up to 5 pages concurrently
                batch = [to_visit.pop(0) for _ in range(min(5, len(to_visit)))]
                
                tasks = []
                for url in batch:
                    if url not in visited:
                        visited.add(url)
                        tasks.append(URLDocumentDownloader.fetch_url_async(url, session))
                
                if not tasks:
                    break
                
                responses = await asyncio.gather(*tasks)
                
                for url, content in zip(batch, responses):
                    if not content:
                        continue
                    
                    print(f"Crawled ({len(visited)}/{max_pages}): {url}")
                    
                    # Convert HTML to text
                    text = URLDocumentDownloader.html_to_text(content)
                    
                    # Extract links for further crawling
                    links = URLDocumentDownloader.extract_links(content, url)
                    for link in links:
                        if link not in visited and link not in to_visit and len(visited) < max_pages:
                            to_visit.append(link)
                    
                    # Save document
                    filename = f"doc_{len(visited)}.md"
                    filepath = os.path.join(output_dir, filename)
                    
                    try:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(f"# Source: {url}\n\n")
                            f.write(text)
                        print(f"  ✓ Saved")
                        saved_count += 1
                    except Exception as e:
                        print(f"  ✗ Error saving: {e}")
        
        print(f"\n✓ Crawl complete! Visited {len(visited)} pages, saved {saved_count} documents")
        return saved_count

    @staticmethod
    def crawl_github_rest_api(start_url: str = "https://docs.github.com/en/rest", 
                              output_dir: str = "data/docs", max_pages: int = 50) -> int:
        """Sync wrapper for crawling GitHub REST API docs (optimized for speed)."""
        # Create new event loop for sync context
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            # No running loop, safe to use asyncio.run()
            return asyncio.run(URLDocumentDownloader.crawl_github_rest_api_async(
                start_url, output_dir, max_pages
            ))
        # In async context, shouldn't be called directly
        raise RuntimeError("Use crawl_github_rest_api_async in async context")

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
