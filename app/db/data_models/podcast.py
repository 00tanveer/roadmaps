# app/db/models/podcast.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func
from app.db.base import Base
from datetime import datetime

class Podcast(Base):
    __tablename__ = "podcasts"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    title: Mapped[str]
    url: Mapped[str]
    original_url: Mapped[str]
    description: Mapped[str]
    author: Mapped[str]
    website: Mapped[str]
    cover_image: Mapped[str]
    language: Mapped[str]  # Could use Enum(LanguageEnum)
    episode_count: Mapped[int]
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    episodes: Mapped[list["Episode"]] = relationship(
        "Episode",
        back_populates="podcast",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return super().__repr__()