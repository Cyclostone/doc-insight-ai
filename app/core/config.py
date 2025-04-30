import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploaded_docs"
VECTOR_STORE_PATH = BASE_DIR / "vectorstore.index"

os.makedirs(UPLOAD_DIR, exist_ok=True)
