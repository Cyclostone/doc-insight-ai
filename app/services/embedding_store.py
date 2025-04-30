from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np 
from app.core.config import VECTOR_STORE_PATH

# Embedder
embedder = SentenceTransformer('all-MiniLM-L6-v2')
dim = embedder.get_sentence_embedding_dimension()

# Load or init index
if VECTOR_STORE_PATH.exists():
    index = faiss.read_index(str(VECTOR_STORE_PATH))
    with open(str(VECTOR_STORE_PATH) + ".pkl", "rb") as f:
        id_to_chunk = pickle.load(f)
else:
    index = faiss.IndexFlatIP(dim)
    id_to_chunk = {}

def add_documents_to_index(chunks, metadata):
    embs = embedder.encode(chunks, convert_to_numpy=True)
    faiss.normalize_L2(embs)
    start = len(id_to_chunk)
    for i, emb in enumerate(embs):
        idx = start + i
        index.add(np.array([emb]))
        id_to_chunk[idx] = {"text": chunks[i], "metadata": metadata}
    
    # Persist
    faiss.write_index(index, str(VECTOR_STORE_PATH))
    with open(str(VECTOR_STORE_PATH) + ".pkl", "wb") as f:
        pickle.dump(id_to_chunk, f)

def search(query_emb, top_k=5):
    faiss.normalize_L2(query_emb)
    D, I = index.search(np.array([query_emb]), top_k)
    return [id_to_chunk[i] for i in I[0] if i in id_to_chunk]

