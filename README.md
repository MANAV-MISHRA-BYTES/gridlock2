# Gridlock 2.0 — ASTraM Command Center

> **Integrated Traffic Intelligence Dashboard** for Bengaluru Urban Mobility & Enforcement  
> Built for the **Flipkart Grid 2.0 Hackathon** in partnership with **Bengaluru Traffic Police**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gridlock2.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

Gridlock 2.0 is a real-time urban traffic intelligence platform designed to serve as a **command-center monitoring system** for city-scale traffic management. It combines spatial demand forecasting with a cascaded computer-vision enforcement pipeline — all wrapped in a high-contrast, institutional dark-mode interface that mirrors actual law enforcement monitoring software.

---

## Features

### Tab 1 — Spatial Demand Forecasting
- Interactive **dark-mode Folium map** centered on Bengaluru (MapmyIndia integration layer)
- 50 dynamically placed **congestion heatmap nodes** color-coded by severity (green → orange → red)
- **CatBoost Ensemble inference** trigger with configurable parameters:
  - Target prediction time
  - Weather condition (Sunny / Rainy / Foggy)
  - Zone filter (Highway / Residential / Street)

### Tab 2 — CCTV Enforcement Pipeline
- **Frame injection** via image upload (JPG / PNG / JPEG)
- Cascaded vision output feed with **bounding box annotations**
- **Live evidence log** with:
  - Violation type detection (Triple Riding, No Helmet)
  - Model confidence scores
  - OCR license plate extraction
- One-click **"Transmit to Control Room"** dispatch button

---

## Tech Stack

| Layer | Technology |
|---|---|
| Dashboard UI | Streamlit |
| Spatial Mapping | Folium + streamlit-folium |
| Computer Vision (headless) | OpenCV |
| Image Processing | Pillow |
| Numerical Engine | NumPy |
| Theme | CartoDB Dark Matter + Institutional Slate |

---

## Live Demo

🔗 **[https://gridlock2.streamlit.app](https://gridlock2-ojh3duebm5gbxmavigoysx.streamlit.app)**  
*(Hosted on Streamlit Community Cloud — no installation required)*

---

## Run Locally

### Prerequisites
- Python 3.9 or higher
- `pip` package manager

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/MANAV-MISHRA-BYTES/gridlock2.git
cd gridlock2

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the dashboard
python -m streamlit run app.py
```

The app will open automatically at **http://localhost:8501**

---

## Deploy on Streamlit Community Cloud

1. Fork or push this repo to your GitHub account
2. Visit [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New App** → select `MANAV-MISHRA-BYTES/gridlock2` → set main file to `app.py`
4. Click **Deploy** — your public URL will be live in under 60 seconds

---

## Project Structure

```
gridlock2/
├── app.py               # Master Streamlit application
├── requirements.txt     # Python dependencies
├── .streamlit/
│   └── config.toml      # Institutional Slate dark theme config
├── .gitignore
└── README.md
```

---

## Theme Configuration

The app enforces a strict command-center aesthetic via `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#0068C9"          # Electric blue — mapping data / UI accents
backgroundColor = "#0E1117"       # Deep slate — primary background
secondaryBackgroundColor = "#262730"  # Elevated panels
textColor = "#FAFAFA"             # High-contrast white text
font = "sans serif"
```

---

## License

MIT — feel free to use, adapt, and build on this for your own traffic intelligence projects.

---

<p align="center">
  Built with precision for the <strong>Flipkart Grid 2.0 Hackathon</strong> &nbsp;|&nbsp; Bengaluru, India
</p>
