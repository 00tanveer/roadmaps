import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import AsyncEngine

from alembic import context

from app.db.session import engine  # your async engine
from app.db.base import Base  # your declarative base
import app.db.data_models.podcast
import app.db.data_models.episode
import app.db.data_models.transcript
import app.db.data_models.transcript_utterance
import app.db.data_models.transcript_word
import app.db.data_models.transcript_chapter

# Interpret the config file for Python logging.
config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=engine.url.render_as_string(hide_password=False),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine

    async with connectable.connect() as connection:
        await connection.run_sync(
            lambda sync_conn: context.configure(
                connection=sync_conn,
                target_metadata=target_metadata,
            )
        )

        await connection.run_sync(
            lambda sync_conn: context.run_migrations()
        )


def run_async_migrations():
    asyncio.run(run_migrations_online())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_async_migrations()
