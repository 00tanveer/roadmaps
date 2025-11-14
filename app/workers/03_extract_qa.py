# Load the transcript object into memory and study them
# from app.language_models.question_detector.src.infer import InferenceModel
import json 
import os
from typing import Dict
import asyncio
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload
from app.db.data_models.transcript_utterance import TranscriptUtterance
from app.db.session import AsyncSessionLocal
from app.db.data_models.podcast import Podcast
from app.db.data_models.episode import Episode
from app.db.data_models.transcript import Transcript
from app.db.data_models.transcript_word import TranscriptWord
from app.db.data_models.transcript_chapter import TranscriptChapter
from app.language_models.question_detector.src.infer import InferenceModel

from app.services.podcasts import read_episode_metadata

questions_model = InferenceModel()

async def episode_metadata(id):
    result = await read_episode_metadata(id)
    print(result)

def is_question(text: str) -> bool:
    if len(text.split()) > 100:
        return False
    score = questions_model.predict(text)[0]
    if score['label'] == 'LABEL_1':
        return True 
    return False

async def main():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            
            # Failed transcripts - 
            # c3f913fc-7fcd-4ae5-a80d-b34f10398cf8
            # 91c07122-a786-4c45-9ac4-ad32d3efe483
            transcript_count_query = select(
                func.count(Transcript.id)
            )
            result = await session.execute(transcript_count_query)
            episodes_count_query = (
                select(
                    Podcast.title.label('pod_title'),
                    func.count(Episode.id)
                )
                .join(Podcast.episodes)
                .where(Podcast.title == "The Peterman Pod")
                .group_by(Podcast.title)
            )
            for r in result:
                print("Transcripts count", r)
            result = await session.execute(episodes_count_query)
            for r in result:
                print(r)
            stmt = (
                select(
                    Podcast.title.label("podcast_title"),
                    Episode.title.label("episode_title"),
                    Episode.duration.label("episode_duration"),
                    func.count(TranscriptWord.id).label("word_count"),
                )
                .join(Podcast.episodes)
                .join(Episode.transcript)
                .join(Transcript.words)
                .join(Transcript.chapters)
                .where(Podcast.title == "The Peterman Pod")
                .group_by(Podcast.title, Episode.title)
            )
            result = await session.execute(stmt)
            for row in result:
                print(f'{row.podcast_title}\n{row.episode_title}\n{row.episode_duration//60}min\n{row.word_count} words\n\n')

# Retrieve host question utterances and store them in episodes
async def extract_questions():
    async with AsyncSessionLocal() as session:
        episodes = (await session.execute(
            select(Episode).options(
                selectinload(Episode.transcript)
                .selectinload(Transcript.utterances)
            )
        )).scalars().all()

        for ep in episodes:
            print("\nTITLE:", ep.title)

            transcript = ep.transcript
            if transcript is None:
                print(f"  ❌ No transcript for episode {ep.id}")
                continue
            guest = guest_speaker(transcript)
            host_questions = []
            for i,u in enumerate(transcript.utterances):
                if u.speaker != guest and is_question(u.text):
                    print("  Q→", u.text)
                    host_questions.append(u)
                    print("  A→", transcript.utterances[i+1].text)
# all_questions = []
# Find speaker with most utterance words
def guest_speaker(transcript: Transcript) -> str:
    speaker_word_count = {}
    for utt in transcript.utterances:
        word_count = len(utt.text.split())
        if utt.speaker in speaker_word_count:
            speaker_word_count[utt.speaker] += word_count
        else:
            speaker_word_count[utt.speaker] = word_count
    # Find speaker with max words
    guest = max(speaker_word_count, key=speaker_word_count.get)
    return guest    

# # print(f"Extracted a total of host {len(all_questions)} questions from {len(transcript_files[:1])} transcripts.")
if __name__ == "__main__":
    # asyncio.run(main())
    asyncio.run(extract_questions())
    # asyncio.run(read_episode_metadata(41867229979))



