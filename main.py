# main.py
from lib.indexer import Indexer
from lib.retrieval import Retriever

def main():
    # Initialize the Indexer
    indexer = Indexer(
        data_dir="data",
        subfolder="insights_json",
        use_remote=False  # use Ollama local embedding endpoint
    )
    retriever = Retriever()
    # Try to load index; if not found, build one
    try:
        questions_index = indexer.load_questions_index()
        print("✅ Index loaded successfully.")
    except FileNotFoundError:
        print("⚠️ No existing index found. Building new index...")
        indexer.build_questions_index()

    # Quick test query
    query = "How to get better at writing?"
    results = retriever.search(query, top_k=10)

    print(f"\nTop results for: {query}")
    for r in results:
        print(f"- {r['question']} (score: {r['similarity']:.3f})")

if __name__ == "__main__":
    main()
