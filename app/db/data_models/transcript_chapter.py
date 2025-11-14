# app/db/models/transcript_chapter.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, DateTime, func
from app.db.base import Base
from datetime import datetime

from app.db.data_models.transcript import Transcript

class TranscriptChapter(Base):
    __tablename__ = "transcript_chapters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transcript_id: Mapped[str] = mapped_column(ForeignKey("transcripts.id", ondelete="CASCADE"))
    summary: Mapped[str]
    headline: Mapped[str]
    gist: Mapped[str] = mapped_column(String, nullable=True)
    start: Mapped[int]
    end: Mapped[int]
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    transcript: Mapped["Transcript"] = relationship(back_populates="chapters")
