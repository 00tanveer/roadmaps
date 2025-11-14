# app/db/models/transcript.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, func
from app.db.base import Base
from datetime import datetime

class Transcript(Base):
    __tablename__ = "transcripts"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    episode_id: Mapped[str] = mapped_column(ForeignKey("episodes.id", ondelete="CASCADE"), unique=True, index=True)
    status: Mapped[str]
    audio_url: Mapped[str]
    text: Mapped[str]
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    episode: Mapped["Episode"] = relationship(back_populates="transcript", uselist=False)
    words: Mapped[list["TranscriptWord"]] = relationship(back_populates="transcript", cascade="all, delete-orphan")
    utterances: Mapped[list["TranscriptUtterance"]] = relationship(back_populates="transcript", cascade="all, delete-orphan")
    chapters: Mapped[list["TranscriptChapter"]] = relationship(back_populates="transcript",
                                                               cascade="all, delete-orphan")
