# app/db/session.py
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.db.base import Base
import os
from app.db.data_models import *

DB_PATH = os.path.expanduser("~/sqlite/stories.db")

DATABASE_URL = "sqlite+aiosqlite:////" + DB_PATH

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
