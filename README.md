# LegalEase: AI-Powered Legal Document Generator

LegalEase creates editable drafts for NDAs, employment contracts, leases, and service agreements. It provides a FastAPI generation API, an optional Gemini integration, a Streamlit interface, and TXT/DOCX/PDF exports.

## Run locally

1. Create a virtual environment and install dependencies: `pip install -r requirements.txt`
2. Optionally copy `.env.example` to `.env` and set `GEMINI_API_KEY`. To use Gemini, additionally install `google-generativeai`.
3. In terminal one: `uvicorn main:app --reload`
4. In terminal two: `streamlit run app.py`

The Streamlit app remains usable if the API is not running, using a local document template draft.

## API

`POST /generate` accepts `document_type`, `parties`, `terms`, and `effective_date`, returning `{ "document": "..." }`.

> LegalEase assists with document drafting and is not a substitute for advice from a qualified legal professional.
