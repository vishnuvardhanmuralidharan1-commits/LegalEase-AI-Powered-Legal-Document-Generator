from fastapi import APIRouter
from pydantic import BaseModel, Field
from ai_core.gemini_generator import GeminiDocumentGenerator

router = APIRouter(tags=["documents"])


class DocumentRequest(BaseModel):
    document_type: str = Field(min_length=2, max_length=100)
    parties: str = Field(min_length=2, max_length=3000)
    terms: str = Field(default="", max_length=8000)
    effective_date: str = Field(min_length=2, max_length=100)


@router.post("/generate")
def generate_document(request: DocumentRequest):
    text = GeminiDocumentGenerator().generate_document(**request.model_dump())
    return {"document": text}
