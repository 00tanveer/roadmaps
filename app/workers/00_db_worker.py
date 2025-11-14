"""
Simple database bootstrap & sandbox worker.
Use this to:
1. Create all database tables defined in app/db/models/*
2. Experiment with SQLAlchemy ORM operations
"""

import asyncio
from app.db.session import AsyncSessionLocal, init_db
from app.db.data_models.podcast import Podcast
from app.db.data_models.episode import Episode
import json
from app.services.podcasts import save_podcast
from app.services.podcasts import save_episodes
from app.services.podcasts import save_transcripts
from sqlalchemy import select
import os

async def setup_database():
    """Create database schema (idempotent)."""
    print("[DB Worker] Initializing database schema...")
    await init_db()
    print("[DB Worker] All tables created (if not existing).")

async def add_podcast_example():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            pod_1 = json.load(open('data/podcasts/podcasts_metadata.json', 'r'))[0]
            await save_podcast(pod_1)
async def get_podcast_titles():
    async with AsyncSessionLocal() as session:
        result = (await session.execute(select(Podcast.title, Podcast.updated_at))).all()
        print(result)

async def main():
    # drop tables and recreate table (no migration support yet)
    await setup_database()
    # save all podcasts from json 
    pods = json.load(open('data/podcasts/podcasts_metadata.json', 'r'))
    await asyncio.gather(*(save_podcast(pod) for pod in pods))
    print(f"✅ Saved {len(pods)} podcasts to database.\n\n")
   
    await get_podcast_titles()
    
    # save episodes from json
    episodes = json.load(open('data/podcasts/pod_episodes_metadata.json', 'r'))
    await save_episodes(episodes)
    print(f"✅ Saved {len(episodes)} episodes to database.")
    
    # save transcripts from json
    transcript_file_paths = os.listdir("data/transcripts/")
    transcripts = []
    for path in transcript_file_paths:
        with open(f"data/transcripts/{path}", 'r') as f:
            transcript = json.load(f)
            transcripts.append(transcript)
    await save_transcripts(transcripts)

if __name__ == "__main__":
    asyncio.run(main())