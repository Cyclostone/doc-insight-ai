from app.services.embedding_store import embedder, search
from app.llm.local_llm import generate_answer

async def answer_query(query: str):
    q_emb = embedder.encode([query], convert_to_numpy=True)[0]
    docs = search(q_emb, top_k=5)
    context = "\n\n".join([d["text"] for d in docs])
    prompt = (
        "Based on the following documents, answer the question in line with institutional values:"
        f"Context: \n{context}\n\nQuestion: {query}\nAnswer:"
    )
    return generate_answer(prompt)