"""Extract DataNodes links from a FitGirl repack page."""
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

FITGIRL_HOST = "fitgirl-repacks.site"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
}


def validate_game_url(url: str) -> str:
    """Only allow pages on the expected FitGirl site."""
    parsed = urlparse((url or "").strip())
    if parsed.scheme not in {"http", "https"} or parsed.hostname not in {FITGIRL_HOST, f"www.{FITGIRL_HOST}"}:
        raise ValueError(f"Please enter a URL from {FITGIRL_HOST}.")
    return parsed.geturl()


def extract_datanodes(url: str) -> list[str]:
    url = validate_game_url(url)
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    found = []
    for container in soup.select("div.dlinks"):
        for anchor in container.select("a[href]"):
            href = anchor.get("href", "").strip()
            if urlparse(href).hostname in {"datanodes.to", "www.datanodes.to"} and href not in found:
                found.append(href)
    return found
