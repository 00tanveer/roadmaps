import chromadb
import json
from datetime import datetime
from app.db.session import AsyncSessionLocal
from app.db.data_models.episode import Episode 
from app.db.data_models.podcast import Podcast
from sqlalchemy import select, and_
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)


class Indexer:
    '''This Indexer class has the abilities to index
        anything inside the Stories project with ChromaDB
    Args:
        chroma_db_dir: Root data folder path.
        subfolder: Subfolder containing JSON files with questions.
        use_remote: Whether to use remote Ollama host.
    '''
    # Indexer class attributes
    CHROMA_HOST = 'localhost'
    EMBEDDING_MODEL = 'mxbai-embed-large:latest'
    OLLAMA_HOST_LOCAL = 'http://localhost:11434'
    OLLAMA_HOST_REMOTE = 'https://ovb1wujcy8gupy-11434.proxy.runpod.net'

    
    def __init__(self):
        self.chroma_client = chromadb.HttpClient(host=self.CHROMA_HOST, port=8000)
        self.ollama_ef = OllamaEmbeddingFunction(
            url=self.OLLAMA_HOST_LOCAL,
            model_name = self.EMBEDDING_MODEL
        )
        self.chroma_coll_config = {
            "hnsw": {
                "space": "cosine",
                "ef_construction": 200,
                "ef_search": 10,
            },
            "embedding_function": self.ollama_ef
        }
        # collections
        self.questions_collection_name = "qa_collection"
        self.qa_collection_name = "episode_qa_pairs"
    
    async def iter_questions_qa(self):
        """Reads all questions from JSON files."""
        async with AsyncSessionLocal() as session:
            async with session.begin():
                stmt = select(
                    Episode,
                    Podcast.author
                ).join(
                    Episode.podcast
                ).where(
                    and_(
                    Episode.host_questions != [],
                    Episode.question_answers != []
                )
                )
                stream = await session.stream(stmt)

                async for row in stream:
                    episode, author = row
                    yield {
                        "id": episode.id,
                        "author": author,
                        "title": episode.title,
                        "podcast_url": episode.podcast_url,
                        "episode_image": episode.episode_image,
                        "enclosure_url": episode.enclosure_url,
                        "duration": episode.duration,
                        "date_published": episode.date_published,
                        "questions": episode.host_questions,
                        "question_answers": episode.question_answers,
                    }
    
    async def iter_questions_qa_batches(self, batch_size=50):
        batch = []
        async for episode in self.iter_questions_qa():
            batch.append(episode)
            if len(batch)>=batch_size:
                yield batch
                batch = []
        if batch:
            yield batch
        
    def init_chroma_collection(self):
        self.questions_collection = self.chroma_client.get_or_create_collection(
            name=self.questions_collection_name,
            configuration=self.chroma_coll_config,
            metadata = {
                "description": "Questions asked by the podcast host in every episode.",
                "created": str(datetime.now())
            }
        )

        self.question_answer_collection = self.chroma_client.get_or_create_collection(
            name=self.qa_collection_name,
            configuration=self.chroma_coll_config,
            metadata = {
                "description": "Question-answer exchanges in every podcast episode.",
                "created": str(datetime.now())
            }
        )
    def sanitize_metadata(self, meta: dict):
        clean = {}
        for k, v in meta.items():
            if v is None:
                clean[k] = ""
                continue

            if isinstance(v, (str, int, float, bool)):
                clean[k] = v
                continue

            if isinstance(v, datetime):
                clean[k] = v.isoformat()
                continue

            if isinstance(v, bytes):
                clean[k] = v.decode("utf-8", errors="ignore")
                continue

            if isinstance(v, (list, dict)):
                clean[k] = json.dumps(v)
                continue

            clean[k] = str(v)

        return clean
    async def upsert_qa_batch(self, episodes_batch):
        questions_collection = self.chroma_client.get_collection(name=self.questions_collection_name)
        ids = []
        documents = []
        metadatas = []

        for episode in episodes_batch:
            doc = {
                "questions": episode["questions"],
                "question_answers": episode["question_answers"]
            }

            metadata = {
                k: v for k, v in episode.items()
                if k not in ("questions", "question_answers")
            }

            clean_metadata = self.sanitize_metadata(metadata)

            ids.append(episode["id"])
            documents.append(json.dumps(doc))
            metadatas.append(clean_metadata)

        # ONE network call, not 50
        questions_collection.add(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
    async def upsert_qa_collection(self, batch_size=5):
        async for batch in self.iter_questions_qa_batches(batch_size=batch_size):
            await self.upsert_qa_batch(batch)

    def delete_collection(self, collection_name):
        try:
            self.chroma_client.delete_collection(collection_name)
            print(f"Deleted collection: {collection_name}")
        except Exception as e:
            print(f"Error: {e}")
            