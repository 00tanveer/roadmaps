from typing import List, Optional
from pydantic import BaseModel, Field

# --- Word-level details ---
class Word(BaseModel):
    text: str
    start: int
    end: int
    confidence: float
    speaker: str

# --- Utterance (speaker-level segment) ---
class Utterance(BaseModel):
    start: int
    end: int
    confidence: float
    speaker: str
    text: str

# --- Chapters Hihglight---
class Chapter(BaseModel):
    headline: Optional[str] = None
    summary: str
    gist: Optional[str] = None
    start: int
    end: int

# --- IAB categories ---
class IABLabel(BaseModel):
    label: str
    relevance: float

class IABResult(BaseModel):
    text: str
    labels: List[IABLabel]

class IABCategoriesResult(BaseModel):
    status: Optional[str]
    results: List[IABResult] = []

# --- Main transcript response ---
class Transcript(BaseModel):
    id: str
    status: str
    audio_url: str
    text: str

    # Optional sub-results
    words: List[Word] = []
    utterances: List[Utterance] = []
    chapters: List[Chapter] = []
    iab_categories_result: Optional[IABCategoriesResult] = None

    # Meta info
    audio_duration: Optional[float] = None
    confidence: Optional[float] = None
    language_code: str
    error: Optional[str] = None
