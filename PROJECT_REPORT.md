# LegalEase: AI-Powered Legal Document Generator

## Project overview

LegalEase is a FastAPI and Streamlit application that helps users produce structured, editable legal-document drafts. It supports non-disclosure agreements, employment contracts, lease agreements, service agreements, and custom agreements.

> LegalEase supports drafting work only. Users should obtain legal-professional review before executing a document.

## Problem statement

Legal documents are often difficult and time-consuming to prepare. LegalEase gives individuals, startups, landlords, freelancers, and professionals a guided way to create an initial draft using their own parties, dates, and terms.

## Technology stack

| Layer | Technology | Purpose |
| --- | --- | --- |
| User interface | Streamlit | Collects document details, displays an editable preview, and supports downloads. |
| API | FastAPI | Validates generation requests and returns document text. |
| AI core | Google Gemini (optional) | Produces AI-assisted drafting when a Gemini API key is configured. |
| Fallback | Python template engine | Produces a well-structured draft when Gemini is not configured or available. |
| Exports | python-docx, fpdf2 | Creates DOCX and PDF documents in addition to TXT downloads. |

## Architecture

```text
Streamlit UI
     |
     | POST /generate
     v
FastAPI (main.py + routes.py)
     |
     v
GeminiDocumentGenerator
     |----------------------------|
     v                            v
Gemini API (optional)      Local safe-template fallback
     |                            |
     +------------> editable legal draft
                              |
                              v
                    TXT / DOCX / PDF export
```

## Key features

1. Selectable legal-document types.
2. Inputs for parties, effective date, and semicolon-separated terms.
3. Gemini-backed generation when `GEMINI_API_KEY` is supplied.
4. Local fallback that keeps the application demonstrable without an API key.
5. Editable in-browser draft and readable legal-style preview.
6. TXT, formatted DOCX, and branded PDF downloads.
7. Clear notice that the output needs legal review.

## How to run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

In a second terminal:

```bash
streamlit run app.py
```

Open the Streamlit address shown in the terminal. To enable Gemini, copy `.env.example` to `.env`, add `GEMINI_API_KEY`, and install `google-generativeai`.

## API example

`POST /generate`

```json
{
  "document_type": "Non-Disclosure Agreement",
  "parties": "Alice (Disclosing Party), Bob (Receiving Party)",
  "terms": "Keep information confidential; Return documents on request",
  "effective_date": "September 24, 2026"
}
```

The endpoint responds with the drafted document in a `document` field.

## Future enhancements

- Clause library with jurisdiction-specific disclaimers.
- Document version history and user accounts.
- E-signature integration.
- Contract-risk highlighting and plain-language summaries.
- Multilingual generation and accessibility enhancements.
