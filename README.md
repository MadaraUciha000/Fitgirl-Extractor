# FITGIRL EXTRACTOR

A small Flask app serving the HTML UI and these JSON endpoints:

- `GET /api/repacks` — fetch up to 50 cards from the popular repacks page.
- `POST /api/extract` — extract DataNodes or FuckingFast URLs from a FitGirl game page.

## Directory map

```text
fitgirl_extractor/
├── app.py                 # Flask app and API routes
├── datanodes.py           # DataNodes link extraction
├── fuckingfast.py         # FuckingFast link extraction
├── fiftyrepacks.py        # Dynamic popular repacks scraper (up to 50)
├── requirements.txt       # Python dependencies
└── templates/
    └── index.html         # Front-end UI
```

## Run locally

Python 3.10+ recommended.

```bash
python -m venv .venv
```

Windows:
```powershell
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install and run:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser. The front end calls the Flask API on the same origin.

## Notes

- The popular-repacks source may return fewer than 50 entries; the scraper displays up to 50 items actually found.
- Network access to the source website is required.
- The extractor only accepts game-page URLs on `fitgirl-repacks.site` (or its `www` host).
