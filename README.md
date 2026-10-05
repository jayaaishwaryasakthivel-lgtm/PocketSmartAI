# PocketSmart AI — Your Smart Budget & Recommendation Assistant

Complete FastAPI + Jinja2 + SQLite + Gemini application based on the supplied PocketSmart AI documentation.

## Features
- User registration, login and logout
- JWT-backed `/token` API
- Session-aware dashboard
- Home Interior Budget Planner
- Party Budget Planner
- Jewelry Budget Planner with optional outfit image
- Gemini multimodal recommendation generation
- Structured recommendation output and budget allocation
- Recommendation history
- Responsive frontend
- Local SQLite persistence
- Demo/fallback recommendations without a Gemini key
- Automated API tests

## VS Code setup

1. Install Python 3.11+.
2. Open this folder in VS Code.
3. Create a virtual environment:
   `python -m venv .venv`
4. Activate it:
   - PowerShell: `.\.venv\Scripts\Activate.ps1`
   - CMD: `.\.venv\Scriptsctivate`
   - macOS/Linux: `source .venv/bin/activate`
5. Install:
   `python -m pip install --upgrade pip`
   `pip install -r requirements.txt`
6. Copy `.env.example` to `.env`.
7. Add `GEMINI_API_KEY=your_key_here` if you want live Gemini generation.
8. Run:
   `uvicorn app.main:app --reload`
9. Open `http://127.0.0.1:8000`.
10. API docs: `http://127.0.0.1:8000/docs`

## Testing
Run:
`pytest -q`

Tests do not require a Gemini key because the application has a deterministic local fallback mode.

## Provider integrations
The source document names Amazon, Flipkart, IKEA, Swiggy, Zomato and OYO. This implementation does not scrape or pretend to use undocumented private APIs. It generates platform-aware search links. Real commercial API/affiliate integrations should be added only through each provider's approved developer program.

## Main API routes
`POST /register`
`POST /login`
`POST /logout`
`POST /token`
`GET /session-info`
`GET /session-data`
`POST /generate-home`
`POST /generate-party`
`POST /generate-jewelry`
`GET /history`
`GET /recommendations-details/{recommendation_id}`
`GET /health`


## Documentation compatibility note
The supplied document describes Flask in one architecture paragraph but later milestones explicitly require FastAPI, `main.py`, FastAPI routes, CORS and Jinja2 templates. This implementation follows those concrete FastAPI requirements. The document names Gemini 1.5 Flash Pro; that model is historical, so the default `.env.example` uses a current Gemini Flash model while `GEMINI_MODEL` remains configurable. Google’s current Gemini API documentation lists current stable Flash models and the `google-genai` Python SDK.
py -3.11 -m venv .venv
