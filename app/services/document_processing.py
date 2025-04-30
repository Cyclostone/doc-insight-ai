import os
import uuid
from fastapi import UploadFile
from app.core.config import UPLOAD_DIR
from app.services.embedding_store import add_documents_to_index
import pdfplumber
import docx 
from nltk.tokenize import sent_tokenize

async def process_documents(file: UploadFile):
    
    # Save File
    ext = os.path.splitext(file.filename)[1].lower()
    unique_name = f"{uuid.uuid4()}{ext}"
    path = UPLOAD_DIR / unique_name
    content = await file.read()
    with open(path, "wb") as f:
        f.write(content)

    # Extract Text
    text = ""
    if ext == ".pdf":
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    elif ext in [".docx", ".doc"]:
        doc = docx.Document(path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        text = content.decode("utf-8", errors="ignore")

    # Chunk
    sentences = sent_tokenize(text)
    chunks, current = [], ""
    max_words = 300

    for sent in sentences:
        if len(current.split()) + len(sent.split()) > max_words:
            chunks.append(current.strip())
            current = sent
        else:
            current += " " + sent 
    
    if current:
        chunks.append(current.strip())

    # Index
    add_documents_to_index(chunks, metadata={"source": file.filename})
    return {"filename": file.filename, "chunks": len(chunks)}


