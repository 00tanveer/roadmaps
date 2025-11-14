# app/db/models/podcast_category.py
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey, DateTime, func
from app.db.base import Base
from datetime import datetime

class PodcastCategory(Base):
    __tablename__ = "podcast_categories"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    transcript_id: Mapped[str] = mapped_column(ForeignKey("transcripts.id"))
    title: Mapped[str]
    description: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
