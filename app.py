"""Flask API and page server for FITGIRL EXTRACTOR."""
from flask import Flask, jsonify, render_template, request
import requests
from datanodes import extract_datanodes
from fuckingfast import extract_fuckingfast
from fiftyrepacks import fetch_top_repacks

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/repacks")
def repacks():
    try:
        data = fetch_top_repacks(50)
        return jsonify(success=True, count=len(data), data=data)
    except requests.RequestException as exc:
        return jsonify(success=False, error=f"Could not fetch the repack list: {exc}"), 502
    except Exception as exc:
        app.logger.exception("Failed to parse repacks")
        return jsonify(success=False, error="Could not parse the repack list."), 500


@app.post("/api/extract")
def extract():
    payload = request.get_json(silent=True) or {}
    url = str(payload.get("url", "")).strip()
    host = str(payload.get("host", "")).strip().lower()
    if host not in {"datanodes", "fuckingfast"}:
        return jsonify(success=False, error="Unsupported host. Choose datanodes or fuckingfast."), 400
    if not url:
        return jsonify(success=False, error="A game page URL is required."), 400
    try:
        links = extract_datanodes(url) if host == "datanodes" else extract_fuckingfast(url)
        return jsonify(success=True, host=host, count=len(links), links=links)
    except ValueError as exc:
        return jsonify(success=False, error=str(exc)), 400
    except requests.RequestException:
        return jsonify(success=False, error="Could not fetch that game page. Check the URL and try again."), 502
    except Exception:
        app.logger.exception("Extraction failed")
        return jsonify(success=False, error="An unexpected extraction error occurred."), 500


if __name__ == "__main__":
    # Debug is off by default; enable only for local development if needed.
    app.run(host="127.0.0.1", port=5000, debug=False)
