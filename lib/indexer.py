import faiss 
import requests
import numpy as np
import json 
from tqdm import tqdm
import os
import hashlib


class Indexer:
    '''This Indexer class has the abilities to index
        anything inside the Stories project.
    Args:
        data_dir: Root data folder path.
        subfolder: Subfolder containing JSON files with questions.
        use_remote: Whether to use remote Ollama host.
    '''
    # Indexer class attributes
    EMBEDDING_MODEL = 'mxbai-embed-large:latest'
    OLLAMA_HOST_LOCAL = 'http://localhost:11434'
    OLLAMA_HOST_REMOTE = 'https://ovb1wujcy8gupy-11434.proxy.runpod.net'
    
    def __init__(self, data_dir="data", subfolder="content_json", use_remote=False):
        self.data_dir = data_dir
        self.folder_path = os.path.join(data_dir, subfolder)
        self.index_path = os.path.join(data_dir, "questions.index")

        if not os.path.exists(self.folder_path):
            raise FileNotFoundError(f"❌ Folder not found: {self.folder_path}")
        
        self.filepaths = [
            os.path.join(self.folder_path, f)
            for f in os.listdir(self.folder_path)
            if os.path.isfile(os.path.join(self.folder_path, f))
        ]
        self.host = self.OLLAMA_HOST_REMOTE if use_remote else self.OLLAMA_HOST_LOCAL
        self.questions = []
        self.questions_index = None
    
    def load_questions(self):
        """Reads all questions from JSON files."""
        questions = []
        for path in self.filepaths:
            with open(path, "r") as f:
                data = json.load(f)
                for block in data['blocks']:
                    questions.append(block["question_text"])
        self.questions = questions
        print(f"📦 Loaded {len(self.questions)} questions.")
        return self.questions
    
    def get_embedding(self, text, model=None):
        model = model or self.EMBEDDING_MODEL
        response = requests.post(
            f"{self.host}/api/embeddings",
            json={"model": model, "prompt": text}
        )
        return np.array(response.json()["embedding"]).astype('float32')

    def build_questions_index(self):
        """Generates embeddings and builds FAISS index."""
        questions = self.load_questions()
        print(questions)
        embeddings = []
        for q in tqdm(questions, desc=f"Generating embeddings for question"):
            print(q)
            vec = self.get_embedding(q)
            if vec is not None and np.isfinite(vec).all():
                embeddings.append(vec)
            else:
                print(f"⚠️ Skipping invalid embedding for question: {q[:50]}...")

        embeddings = np.array(embeddings, dtype=np.float32)
       # Normalize vectors for cosine similarity
        faiss.normalize_L2(embeddings)
        # Build FAISS index
        dim = embeddings.shape[1]
        index = faiss.IndexFlatIP(dim)  # cosine similarity
        index.add(embeddings)

        self.questions_index = index
        faiss.write_index(index, "data/questions.index")

        print(f"💾 Saved FAISS index with {index.ntotal} vectors.")

    def load_questions_index(self, path="data/questions.index"):
        """Loads FAISS index from disk."""
        path = path or self.index_path
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ Index file not found: {path}")
        self.questions_index = faiss.read_index(path)
        print(f"✅ Loaded index from {path}")
        return self.questions_index