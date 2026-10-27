"""Extract FuckingFast links from a FitGirl repack page."""
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
from datanodes import validate_game_url, HEADERS


def extract_fuckingfast(url: str) -> list[str]:
    url = validate_game_url(url)
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    found = []
    for container in soup.select("div.dlinks"):
        for anchor in container.select("a[href]"):
            href = anchor.get("href", "").strip()
            if urlparse(href).hostname in {"fuckingfast.co", "www.fuckingfast.co"} and href not in found:
                found.append(href)
    return found
