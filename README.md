# DASH-Apps

# DASH-Apps

Simple collection of Plotly Dash example apps — a personal playground while I learn Dash. Not production-ready; just for experimenting and prototyping.

## About
This repository contains small, self-contained Dash apps, example layouts and helper scripts I use to practice building interactive dashboards with Python and Plotly.

## Quick start
1. Clone:
```bash
git clone https://github.com/RATHOD-SHUBHAM/DASH-Apps.git
cd DASH-Apps
```

2. (Optional but recommended) Create a virtualenv:
```bash
uv venv --python 3.11
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate
```

3. Install minimal dependencies:
```bash
uv pip install -r requirements.txt
```

## Run an app
Run any app file in the `apps/` folder (or root) like:
```bash
uv run apps/example_app.py
```
Open http://127.0.0.1:8050 in your browser (port may vary).

## Notes
- This repo is for learning only — expect quick experiments, hacks and rough code.
- No strict API stability or production configs are provided.
- Feel free to reorganize or delete example files as you learn.
