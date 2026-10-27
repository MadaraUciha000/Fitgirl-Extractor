"""Fetch popular repack cards and resolve WordPress lazy-loaded cover URLs."""
import html
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

POPULAR_URL = "https://fitgirl-repacks.site/pop-repacks/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
}

def _best_image_url(image, page_url: str) -> str:
    # WordPress themes/plugins may keep the real cover in a lazy-load attribute.
    for attr in ("data-lazy-src", "data-src", "data-original", "data-orig-file", "data-full-url", "src"):
        value = (image.get(attr) or "").strip()
        if value and not value.startswith("data:"):
            return urljoin(page_url, value)
    # Responsive image sets are a useful fallback if src is a transparent placeholder.
    for attr in ("data-srcset", "srcset"):
        value = (image.get(attr) or "").strip()
        if value:
            candidates = []
            for part in value.split(","):
                bits = part.strip().split()
                if bits and not bits[0].startswith("data:"):
                    width = 0
                    if len(bits) > 1 and bits[1].endswith("w"):
                        try:
                            width = int(bits[1][:-1])
                        except ValueError:
                            pass
                    candidates.append((width, urljoin(page_url, bits[0])))
            if candidates:
                return max(candidates, key=lambda item: item[0])[1]
    return ""

def fetch_top_repacks(limit: int = 50) -> list[dict[str, str]]:
    response = requests.get(POPULAR_URL, headers=HEADERS, timeout=25)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    article = soup.find("article", class_="page") or soup
    content = article.find("div", class_="entry-content") or soup
    results: list[dict[str, str]] = []
    seen: set[str] = set()

    for item in content.select(".widget-grid-view-image a[href]"):
        image = item.find("img")
        title = (item.get("title") or "").strip()
        if image:
            title = title or (image.get("alt") or image.get("title") or "").strip()
        game_url = urljoin(POPULAR_URL, (item.get("href") or "").strip())
        cover = _best_image_url(image, POPULAR_URL) if image else ""
        if title and game_url and game_url not in seen:
            seen.add(game_url)
            results.append({
                "title": html.unescape(title),
                "url": game_url,
                "cover": cover,
            })
        if len(results) >= max(1, min(int(limit), 50)):
            break
    return results
