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
from app.language_models.question_detector.src.infer import InferenceModel

from app.services.podcasts import read_episode_metadata

questions_model = InferenceModel()

def is_question(text: str) -> bool:
    if len(text.split()) > 100:
        return False
    score = questions_model.predict(text)[0]
    if score['label'] == 'LABEL_1':
        return True 
    return False

async def main():
    results = await extract_questions()
    await save_question_results(results)
    print("🎉 All questions & answers saved!")

sem = asyncio.Semaphore(10)
async def questions_from_one_episode(ep):
    async with sem:
        try:
            print("\nTITLE:", ep.title)
            transcript = ep.transcript
            if transcript is None:
                print(f"  ❌ No transcript for episode {ep.id}")
                return None
            guest = guest_speaker(transcript)
            host_questions = []
            question_answers = []
            for i,u in enumerate(transcript.utterances):
                if u.speaker != guest and is_question(u.text):
                    question = u.text
                    # print("  Q→", question)
                    host_questions.append(question)
                    answer = transcript.utterances[i+1].text
                    question_answers.append(
                        {"question": u.text, "answer": answer}
                    )
                    # print("  A→", answer)
            # ep.host_questions = host_questions
            # ep.question_answers = question_answers

            return {
                "episode_id": ep.id,
                "guest": guest,
                "host_questions": host_questions,
                "question_answers": question_answers
            }
        except Exception as e:
            print(f'❌ Failed extracting questions from episode {ep.title}: {e}')
# Retrieve host question utterances and store them in episodes
async def extract_questions():
    async with AsyncSessionLocal() as session:
        episodes = (await session.execute(
            select(Episode).options(
                selectinload(Episode.transcript)
                .selectinload(Transcript.utterances)
            )
        )).scalars().all()

        # detach objects so they are usable safely in workers
        for ep in episodes:
            session.expunge(ep)
        tasks = [
            questions_from_one_episode(ep)
            for ep in episodes
        ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [r for r in results if r is not None]
async def save_question_results(results):
    async with AsyncSessionLocal() as session:
        async with session.begin():
            for r in results:
                ep = await session.get(Episode, r["episode_id"])
                ep.host_questions = r["host_questions"]
                ep.question_answers = r["question_answers"]
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
    asyncio.run(main())



