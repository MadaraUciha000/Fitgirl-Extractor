<div align="center">

# 🎮 FITGIRL EXTRACTOR

### A Modern Game Link Extraction & Repack Discovery Interface

A sleek, glassmorphic web application for browsing popular game pages, extracting supported download-host links, and discovering batch downloader tools.

<br>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Modern UI · Responsive Design · Flask API · Dynamic Game Listings**

</div>

---

## ✨ Overview

**FITGIRL EXTRACTOR** is a lightweight web interface that combines game-page discovery, supported download-link extraction, and links to third-party batch downloader applications.

The application uses Flask for its backend and HTML, CSS, and JavaScript for its frontend. Its design features animated backgrounds, glassmorphism, responsive game cards, and customizable accent colours.

## 🚀 Features

### 🎮 Game Discovery
- Dynamically retrieve popular game listings from the configured source.
- Display game titles and cover artwork.
- Search the game list instantly.
- Open individual game pages directly.
- Display up to 50 popular listings.

### 🔗 Link Extraction
- **DataNodes:** Extract supported DataNodes links from game pages.
- **FuckingFast:** Extract supported FuckingFast links from game pages.
- Copy extracted links to the clipboard.
- Clear results and start another extraction.
- Display success, empty-result, and error states.

### 📥 Batch Downloader Resources
- MoonDownloader resource and installer page.
- FuckingFast Downloader Windows installer.
- Links to official project release pages where available.
- Embedded application screenshots.

### 🎨 User Interface
- Dark interface with glassmorphic panels.
- Animated wave background.
- Rounded cards, buttons, and image containers.
- Responsive layout for desktop, tablet, and mobile.
- Six accent themes: lime, red, blue, pink, purple, and white.
- Animated bottom navigation.
- Searchable game cards and SVG icons.
- Structured footer with navigation and resource links.

### ⚙️ Backend
- Flask application with JSON API routes.
- Separate modules for each supported link extractor.
- Dedicated module for retrieving popular game listings.
- Request timeouts and basic error handling.

---

## 🖥️ Preview

The interface includes the following sections:

| Section | Description |
|---|---|
| Home | Introduction and quick links to supported hosts |
| Popular Repacks | Searchable game cards with cover images |
| DataNodes Extractor | Extract supported DataNodes links |
| FuckingFast Extractor | Extract supported FuckingFast links |
| Batch Downloaders | Links to downloader resources and installers |
| Theme Selector | Switch between six accent colours |
| Footer | Navigation and external resources |

---

## 📁 Project Structure

```text
fitgirl-extractor/
│
├── app.py                 # Flask application and API routes
├── datanodes.py           # DataNodes link extraction
├── fuckingfast.py         # FuckingFast link extraction
├── fiftyrepacks.py        # Popular game listing scraper
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel deployment configuration
├── README.md              # Project documentation
│
└── templates/
    └── index.html         # Frontend interface
```

---

## 🛠️ Requirements

- Python 3.10 or newer recommended.
- pip package manager.
- Internet connection for retrieving remote game listings and extracting links.
- A supported operating system: Windows, Linux, or macOS.

---

## 📦 Installation

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/fitgirl-extractor.git
```

### 2. Open the project directory

```bash
cd fitgirl-extractor
```

### 3. Create a virtual environment (recommended)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

If you have not created `requirements.txt` yet, use:

```text
Flask
requests
beautifulsoup4
```

### 5. Start the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Keep the Flask process running while using the application.

---

## 🔌 API Documentation

The frontend communicates with the Flask backend through JSON endpoints.

### `GET /api/repacks`

Retrieves the configured popular game listings.

**Example request:**

```http
GET /api/repacks
```

**Expected response structure:**

```json
{
  "success": true,
  "count": 2,
  "data": [
    {
      "title": "Example Game",
      "url": "https://example.com/game/",
      "cover": "https://example.com/cover.jpg"
    }
  ]
}
```

The example illustrates the expected response structure; it is not a live API result.

### `POST /api/extract`

Extracts supported links from a game-page URL.

**Request body:**

```json
{
  "url": "https://fitgirl-repacks.site/example-game/",
  "host": "datanodes"
}
```

Set `host` to either:

- `datanodes`
- `fuckingfast`

**Expected response structure:**

```json
{
  "success": true,
  "host": "datanodes",
  "count": 2,
  "links": [
    "https://datanodes.to/example1",
    "https://datanodes.to/example2"
  ]
}
```

These are illustrative examples. Actual results depend on the backend implementation and the source page.

---

## 🌐 Deployment

### Deploying to Vercel

The repository includes a `vercel.json` configuration for the Python runtime.

1. Push the project to GitHub.
2. Import the repository into your Vercel account.
3. Check the Python runtime and project configuration.
4. Deploy the application.
5. Test the homepage and API endpoints.

**Deployment considerations:**

- Serverless execution limits may affect scraping requests.
- The source website may block automated requests.
- Remote image hosts may restrict embedded images.
- Scraping results depend on the source website's current HTML structure.
- A successful deployment does not guarantee that every external source is accessible.

For production deployments, configure appropriate timeouts, logging, and error responses.

---

## 🔧 Configuration

### Frontend

The primary frontend file is:

```text
templates/index.html
```

You can modify:

- Accent colours and theme variables.
- Card spacing and image proportions.
- Navigation labels.
- Animations and glassmorphic styling.
- Downloader resource links.
- Footer content.

### Backend

The backend modules are separated by responsibility:

| File | Responsibility |
|---|---|
| `app.py` | Flask routes and request handling |
| `datanodes.py` | DataNodes link extraction |
| `fuckingfast.py` | FuckingFast link extraction |
| `fiftyrepacks.py` | Popular game listing retrieval |

Keep the extraction logic in its corresponding module to make maintenance easier.

---

## 🛡️ Security & Responsible Use

- Use only sources and content you are authorized to access.
- Respect website terms, copyright, and applicable laws.
- Review third-party installers before executing them.
- Never expose API keys, credentials, or private configuration in a public repository.
- Validate user-supplied URLs on the server.
- Apply request timeouts and sensible rate limits.
- Avoid exposing internal exceptions or sensitive server details to users.
- Do not use the application to bypass access controls or download content without authorization.

This project does not guarantee the safety, availability, or integrity of third-party websites, download links, or installers.

---

## 🐛 Troubleshooting

### Game listings do not appear

- Confirm the Flask server is running.
- Open `/api/repacks` directly to inspect its response.
- Check the terminal for request or parsing errors.
- Verify that the configured source website is accessible.

### Cover images are missing

- Check whether the image URL opens directly in your browser.
- Confirm that the source returns a valid image.
- Check for hotlink protection or expired image URLs.
- Inspect browser developer tools for image-loading errors.

### Link extraction returns no results

- Confirm that the game-page URL is valid.
- Verify that the page contains links for the selected host.
- Check whether the website has changed its HTML structure.
- Review the Flask terminal output for request failures.

### Vercel deployment fails

- Check the build logs.
- Confirm `app.py` exposes the Flask application as `app`.
- Verify that dependencies are declared in `requirements.txt`.
- Check that the runtime configuration matches the deployed project structure.

---

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application locally.
5. Submit a pull request describing your changes.

For larger changes, open an issue first to discuss the proposed implementation.

---

## 📄 License

This project can be distributed under the MIT License if you choose to license it that way. Add a `LICENSE` file containing the appropriate license text before claiming that the repository is officially MIT-licensed.

---

## ⚠️ Disclaimer

FITGIRL EXTRACTOR is an independent community project. It is not affiliated with, endorsed by, or officially associated with FitGirl Repacks, DataNodes, FuckingFast, MoonDownloader, or their respective owners.

All trademarks, application names, and external resources belong to their respective owners. This project provides an interface for working with publicly accessible pages and supported links; users are responsible for ensuring their use complies with applicable laws and third-party terms.

<div align="center">

**Built for a cleaner, smoother browsing experience.**

</div>
```

### Before publishing

1. Replace `YOUR_USERNAME` with your actual GitHub username.
2. Verify the repository name and all source URLs.
3. Add a `LICENSE` file if you intend to publish under a specific license.
4. Confirm the API response formats match your actual Flask implementation.

**Recommended filename:** `README.md` — save it in the root directory beside `app.py` and `vercel.json`.
