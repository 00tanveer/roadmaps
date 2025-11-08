# main.py
from lib.indexer import Indexer
from lib.retrieval import Retriever
import numpy as np

def main():
    # Initialize the Indexer
    indexer = Indexer(
        data_dir="data",
        subfolder="content_json",
        use_remote=False  # use Ollama local embedding endpoint
    )
    # Try to load index; if not found, build one
    try:
        questions_index = indexer.load_questions_index()
        print("✅ Index loaded successfully.")
    except FileNotFoundError:
        print("⚠️ No existing index found. Building new index...")
        indexer.build_questions_index()

    # def cosine(a, b): return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # q1 = "How to get better in writing?"
    # q2 = "When you talk about the individual con contributions, ‘cause you mentioned that was your way of having a lot of impact, do you have a way of thinking about which contributions are more impactful than others? "
    # v1 = indexer.get_embedding(q1)
    # v2 = indexer.get_embedding(q2)
    # print("Cosine:", cosine(v1, v2))
    # Quick test query
    query = "How to get better in writing?"
    retriever = Retriever()
    results = retriever.search(query, top_k=10)

    print(f"\nTop results for: {query}")
    for r in results:
        print(f"- {r['question']} (score: {r['similarity']:.3f})")

if __name__ == "__main__":
    main()
