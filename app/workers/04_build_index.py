import chromadb
from app.services.indexer import Indexer
import asyncio

chroma_client = chromadb.HttpClient(host="localhost", port=8000)


async def main():
    indexer = Indexer()
    indexer.init_chroma_collection()
    await indexer.upsert_qa_collection()

    # indexer.delete_collection("episode_qa_pairs")

if __name__ == "__main__":
    asyncio.run(main())