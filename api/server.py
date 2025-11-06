from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from lib.indexer import Indexer
from lib.retrieval import Retriever
import uvicorn
import threading

app = FastAPI(title="Stories Search API", version="1.0")

# ---- Initialize the Indexer (singleton)
indexer = Indexer(data_dir="data", subfolder="insights_json", use_remote=False)
retriever = Retriever(data_dir="data", subfolder="insights_json")
# Try loading an existing index; fallback to rebuild
try:
    print(indexer.load_questions_index())
except FileNotFoundError:
    print("⚠️ No existing index found, building a new one...")
    threading.Thread(target=indexer.build_questions_index).start()

# ---- Request/Response Models ----
class QueryRequest(BaseModel):
    query: str
    top_k: int = 10

# ---- Routes ----
@app.get("/")
def root():
    return {"message": "Stories Indexer API is live 🚀"}


@app.post("/search")
def search(request: QueryRequest):
    """Perform a semantic search against indexed questions."""
    try:
        results = retriever.search(request.query, top_k=request.top_k)
        return {"query": request.query, "results": results}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/reindex")
def reindex():
    """Rebuilds the FAISS index from source JSON files."""
    threading.Thread(target=indexer.build_index).start()
    return {"message": "Index rebuilding started in background."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
