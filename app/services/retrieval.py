from app.services.indexer import Indexer
from FlagEmbedding import FlagModel
from collections import Counter

class Retriever:
    """
    Handles semantic search over indexed data.
    Uses FAISS for similarity search and Indexer for embeddings.
    """
    EMBEDDING_MODEL = 'BAAI/bge-base-en-v1.5'
    def __init__(self):
        self.query_emb_model = FlagModel(self.EMBEDDING_MODEL, devices='cpu')
        self.chroma_client = Indexer()
        self.qa_collection = self.chroma_client.get_collection(name="episode_qa_pairs")

    def search(self, query_text, top_k=10, threshold=0.45):
        """Search top-k similar questions."""
        embedding = self.query_emb_model.encode(query_text)
        # print(embedding)
        results = self.qa_collection.query(query_embeddings=embedding, n_results=top_k)
        # print(results)
        return results
    
    def count_duplicates(self):
        print(self.qa_collection.count())
        res = self.qa_collection.get()
        docs = res["documents"]  # Chroma wraps it inside a list
        counts = Counter(docs)

        duplicates = {doc: count for doc, count in counts.items() if count > 1}

        print("Total docs:", len(docs))
        print("Unique docs:", len(counts))
        print("Duplicate docs:", sum(count - 1 for count in counts.values() if count > 1))
        print("Number of distinct duplicated texts:", len(duplicates))

       

