import html
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

def fetch_top_repacks():
    url = "https://fitgirl-repacks.site/pop-repacks/"
    # Headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")

    # Locate the container for 'Most Popular Repacks'
    article = soup.find("article", class_="page")
    if not article:
        article = soup

    content_area = article.find("div", class_="entry-content")
    if not content_area:
        content_area = soup

    top_repacks = []
    items = content_area.select(".widget-grid-view-image a")

    for item in items:
        title = item.get("title")
        img = item.find("img")
        cover_url = ""
        
        if img:
            if not title:
                title = img.get("alt", "")
            cover_url = img.get("src", "")

        game_url = item.get("href", "")

        if title and game_url:
            clean_title = html.unescape(title.strip())
            top_repacks.append({
                "title": clean_title, 
                "url": game_url.strip(),
                "cover": cover_url.strip()
            })

    return top_repacks

@app.route('/api/repacks', methods=['GET'])
def get_repacks():
    try:
        data = fetch_top_repacks()
        return jsonify({
            "success": True,
            "count": len(data),
            "data": data
        }), 200
    except requests.exceptions.RequestException as e:
        return jsonify({
            "success": False,
            "error": f"Failed to fetch data from the website: {str(e)}"
        }), 502
    except Exception as e:
        return jsonify({
            "success": False,
            "error": f"An error occurred while parsing data: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)