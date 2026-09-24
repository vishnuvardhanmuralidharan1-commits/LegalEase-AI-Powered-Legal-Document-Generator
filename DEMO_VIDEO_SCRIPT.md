# LegalEase Demo Video Script (3-4 minutes)

## 1. Introduction (0:00-0:25)

“Hello, this is LegalEase: AI-Powered Legal Document Generator. LegalEase helps users create editable drafts for commonly used legal documents such as NDAs, employment contracts, leases, and service agreements. It is designed to make the first drafting step faster and easier while clearly reminding users to obtain professional legal review.”

## 2. Architecture (0:25-0:50)

“The application uses Streamlit for the frontend and FastAPI for the backend. FastAPI validates the user’s request and sends it to the document-generation component. When configured, the component can use Google Gemini. It also contains a local fallback template, so the project remains fully demonstrable without an API key. The user can then edit and export the document.”

## 3. Enter document information (0:50-1:35)

Show the Streamlit page. Select **Non-Disclosure Agreement**. Enter:

- Parties: `Alice (Disclosing Party), Bob (Receiving Party)`
- Terms: `Keep information confidential; Use information only for the project; Return documents on request`
- Effective date: select today’s date.

“The form gathers only the essential information: document type, parties, terms, and effective date. Terms are separated using semicolons and are transformed into structured clauses.”

## 4. Generate and edit (1:35-2:25)

Click **Generate document**.

“LegalEase returns a structured draft with headings for parties, purpose, terms, confidentiality, termination, governing law, and signatures. The document remains editable. This gives users control over the final language before any download.”

Make a short edit in the draft, such as adding a term or modifying a party name.

## 5. Export formats (2:25-3:00)

Click each of the three download controls: **TXT**, **DOCX**, and **PDF**.

“The same reviewed text can be exported as a plain TXT file, a formatted Microsoft Word document, or a branded PDF with header and footer. This supports both simple sharing and professional presentation.”

## 6. Conclusion (3:00-3:20)

“LegalEase demonstrates how Generative AI can improve access to legal-document drafting while preserving user editing control and responsible legal-review guidance. Thank you.”
