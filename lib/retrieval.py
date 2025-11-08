import os
import json
import faiss
from lib.indexer import Indexer
import numpy as np

class Retriever:
    """
    Handles semantic search over indexed data.
    Uses FAISS for similarity search and Indexer for embeddings.
    """

    def __init__(self, data_dir="data", subfolder="content_json", index_filename="questions.index", use_remote=False):
        self.data_dir = data_dir
        self.folder_path = os.path.join(data_dir, subfolder)
        self.index_path = os.path.join(data_dir, index_filename)
        self.indexer = Indexer(data_dir, subfolder, use_remote)
        self.questions_index = self.indexer.load_questions_index()
        self.qa = self.load_qa()

    def load_qa(self):
        """Load all questions from JSON files."""
        qa = []
        for f in os.listdir(self.folder_path):
            path = os.path.join(self.folder_path, f)
            if not os.path.isfile(path):
                continue
            with open(path, "r") as file:
                data = json.load(file)
                for block in data['blocks']:
                    if "question_text" in block:
                        qa.append((block["question_text"], block['answer_text'], block['start_time']))
        print(f"✅ Loaded {len(qa)} question-answer pairs from {self.folder_path}")
        return qa

    def search(self, query_text, top_k=10, threshold=0.45):
        """Search top-k similar questions."""
        query_vec = self.indexer.get_embedding(query_text).reshape(1, -1).astype(np.float32)
        faiss.normalize_L2(query_vec)

        # sanity check
        if np.any(~np.isfinite(query_vec)):
            print("❌ Invalid query embedding:", query_vec)
            return []
        
        print(f"🔍 Searching for: {query_text}")
        D, I = self.questions_index.search(query_vec, top_k)

        results = []
        for idx, score in zip(I[0], D[0]):
            if idx < len(self.qa) and score > threshold:
                q, a, t = self.qa[idx]
                results.append({
                    "question": q,
                    "similarity": round(float(score),4),
                    "answer": a,
                    "start_time": t
                })
        return results
