import os


class GeminiDocumentGenerator:
    """Generate a draft with Gemini when configured, otherwise a safe local template."""

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

    def generate_document(self, document_type: str, parties: str, terms: str, effective_date: str) -> str:
        prompt = self._prompt(document_type, parties, terms, effective_date)
        if self.api_key:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                response = genai.GenerativeModel(self.model_name).generate_content(prompt)
                if response.text:
                    return response.text.strip()
            except Exception:
                pass
        return self._local_draft(document_type, parties, terms, effective_date)

    @staticmethod
    def _prompt(document_type, parties, terms, effective_date):
        return f"""Draft a clear, professional {document_type}. Parties: {parties}. Effective date: {effective_date}. Terms: {terms}.
Use headings, numbered clauses, and plain professional language. Do not claim this is legal advice; add a short review notice."""

    @staticmethod
    def _local_draft(document_type, parties, terms, effective_date):
        clauses = [item.strip() for item in terms.split(";") if item.strip()]
        clause_text = "\n".join(f"{i}. {clause}" for i, clause in enumerate(clauses, 1)) or "1. The parties will agree on the applicable terms in writing."
        return f"""{document_type.upper()}

This {document_type} (the \"Agreement\") is made effective as of {effective_date}.

PARTIES
This Agreement is entered into by and among: {parties} (collectively, the \"Parties\").

PURPOSE
The Parties wish to record their understanding and the terms governing their relationship in a clear written form.

TERMS AND CONDITIONS
{clause_text}

CONFIDENTIALITY
Each Party will protect non-public information received in connection with this Agreement and will use it only for the purposes described here, except where disclosure is required by law.

TERM AND TERMINATION
This Agreement begins on the effective date and remains in force until completed or terminated by either Party with written notice, subject to obligations that reasonably survive termination.

GOVERNING LAW
The Parties will determine the governing law and dispute-resolution process appropriate to their jurisdiction before signing.

SIGNATURES
By signing below, the Parties acknowledge that they have read and understood this Agreement.

______________________________        ______________________________
Authorized representative                Authorized representative

Important: This AI-generated draft is for informational purposes and should be reviewed by a qualified legal professional before use."""
