from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.document_processing import process_documents
from app.services.query_handler import answer_query

router = APIRouter()

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        return await process_documents(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query")
async def query(payload: dict):
    query_text = payload.get("query")
    if not query_text:
        raise HTTPException(status_code=400, detail=str(e))
    try:
        return {"answer": await answer_query(query_text)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

