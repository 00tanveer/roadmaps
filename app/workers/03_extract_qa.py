# Load the transcript object into memory and study them
from app.data_models.transcript import Transcript
from app.language_models.question_detector.src.infer import InferenceModel
import json 
import os
from pydantic import ValidationError
from pathlib import Path
import sqlite3
import pickle

transcript_files = os.listdir("data/transcripts/")
questions_model = InferenceModel()

''' 
    Persistent idempotent store all transcripts in the TranscriptStore
    - Uses SQLite for indexing
    - Pickle for fast object serialization
'''
class TranscriptStore:
    def __init__(self, path="data/transcripts/transcripts_cache.db"):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS transcripts (id TEXT PRIMARY KEY, blob BLOB)")
    def save(self, transcript: Transcript):
        serialized = pickle.dumps(transcript, protocol=pickle.HIGHEST_PROTOCOL)
        existing = self.conn.execute(
            "SELECT blob FROM transcripts WHERE id = ?", (transcript.id,)
        ).fetchone()

        # Compare before writing (saves unnecessary disk I/O)
        if existing and existing[0] == serialized:
            return  # No changes, skip writing

        self.conn.execute("""
            INSERT INTO transcripts (id, blob)
            VALUES (?, ?)
            ON CONFLICT(id) DO UPDATE SET
                blob = excluded.blob
        """, (transcript.id, serialized))
        self.conn.commit()

    def load(self, transcript_id: str) -> Transcript | None:
        cur = self.conn.execute("SELECT blob FROM transcripts WHERE id=?", (transcript_id,))
        row = cur.fetchone()
        return pickle.loads(row[0]) if row else None

    def all(self) -> list[Transcript]:
        cur = self.conn.execute("SELECT blob FROM transcripts")
        return [pickle.loads(r[0]) for r in cur.fetchall()]
    def close(self):
        self.conn.close()


store = TranscriptStore()
# for file in transcript_files:
#     with open(f'data/transcripts/{file}', 'r') as f:
#         data = json.load(f)
#         try:
#             transcript = Transcript(**data)
#             store.save(transcript)
#         except ValidationError as e:
#             print("\n⚠️ Validation error for transcript ID:", data.get("id"))
#             print("Status:", data.get("status"))
#             print("Audio URL:", data.get("audio_url"))
#             print("Fields returned:", [k for k in data.keys()])
#             print("Raw values of failed fields:")
#             # print({field: data.get(field) for field in ["words", "utterances", "chapters"]})
#             raise

pods = json.load(open('data/podcasts/podcasts_metadata.json', 'r'))
eps_json = json.load(open("data/podcasts/pod_episodes_metadata.json", 'r'))
# Get list of the IDS of the transcripts I want to analyze first
target_pods = [
    'The Peterman Pod',
    'A Life Engineered'
]
target_episodes = {}
for pod in pods:
    pod_title = pod.get('title', 'unknown_podcast').replace('/', '_').replace('\\', '_')
    if (pod_title in target_pods):
        pod_dir = os.path.join('data/podcasts/', pod_title)
        # if {episode_title}_transcript.txt doesn't exist, create it
        for ep in eps_json:
            if ep['feedId'] == pod['id']:
                episode_title = ep.get('title', 'unknown_episode').replace('/', '_').replace('\\', '_')
                transcript_path = os.path.join(pod_dir, f"{episode_title}_transcript.txt")
                t_id = json.load(open(transcript_path, 'r'))['id']
                target_episodes.append(t_id)
# Load only target transcripts from the store
transcripts = []
for t_id in target_episodes:
    transcript = store.load(t_id)
    if transcript:
        transcripts.append(transcript)
for t in transcripts:
    print(f"Loaded Transcript ID: {t.id}, Duration: {t.audio_duration//60}, Utterances: {len(t.utterances)}")
# transcripts = store.all()
# print(type(transcripts))
# store.close()



def summary(transcript_files):
    # get all transcript json filepaths in directory data/transcripts/
    # print(transcript_files)

    transcripts = []
    for file in transcript_files:
        with open(f'data/transcripts/{file}', 'r') as f:
            data = json.load(f)
            try:
                transcript = Transcript(**data)
            except ValidationError as e:
                print("\n⚠️ Validation error for transcript ID:", data.get("id"))
                print("Status:", data.get("status"))
                print("Audio URL:", data.get("audio_url"))
                print("Fields returned:", [k for k in data.keys()])
                print("Raw values of failed fields:")
                # print({field: data.get(field) for field in ["words", "utterances", "chapters"]})
                raise
            transcripts.append(transcript)

    # Explore the transcript object structure
    for i, transcript in enumerate(transcripts):
        print(f"=== Transcript Metadata {i} {transcript.id}===")
        print(f"Audio duration: {transcript.audio_duration}")
        print(f"Number of words: {len(transcript.words)}")
        print(f"Number of utterances: {len(transcript.utterances)}")
        print(f"Number of chapters: {len(transcript.chapters)}")
        print(f"Number of IAB categories: {len(transcript.iab_categories_result.results) if transcript.iab_categories_result else 0}")
        #number of utterances

    # count how many transcripts have just one speaker in utterances and print which ones
    single_speaker_count = 0
    for transcript in transcripts:
        speakers = set(utt.speaker for utt in transcript.utterances)
        if len(speakers) == 1:
            single_speaker_count += 1
            print(f"Transcript ID with single speaker: {transcript.id}, Speaker: {speakers.pop()}")
            #delete these transcript files from data/transcripts/
            os.remove(f"data/transcripts/{transcript.id}.json")
  

# Print question utterances from just one transcript 

def is_question(text: str) -> bool:
    # Use our own trained distilbert-based model for question detection
    # First filter out text great than 500 tokens
    if len(text.split()) > 100:
        return False
    # print(f'\nClassifying text: {text}')
    score = questions_model.predict(text)[0]
    # print(f'Prediction score: {score}')
    if score['label'] == 'LABEL_1':
        return True
    return False
def extract_questions(transcript: Transcript):
    questions = []
    for utt in transcript.utterances:
        if is_question(utt.text):
            questions.append({
                "speaker": utt.speaker,
                "question_text": utt.text,
                "start_time": utt.start,
                "end_time": utt.end
            })
    return questions
all_questions = []
# Find speaker with most utterance words
def guest_speaker(transcript: Transcript):
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

# Find questions from host (not guest) speaker
for file in transcript_files:
    with open(f'data/transcripts/{file}', 'r') as f:
        data = json.load(f)
    transcript = Transcript(**data)
    print(f"Processing Transcript ID: {transcript.id}")
    guest = guest_speaker(transcript)
    utterances = transcript.utterances
    #Get utterances that are not from guest speaker
    host_utterances = [u for u in utterances if u.speaker != guest]
    # Print host utterances
    # for u in host_utterances:
    #     print(f"Host Utterance: {u.text} (Speaker: {u.speaker})")
    # Questions within host_utterances
    host_questions = [u for u in host_utterances if is_question(u.text)]
    # for q in host_questions:
    #     print(f"Host Question: {q.text} (Speaker: {q.speaker}, Start: {q.start}, End: {q.end})")
    # Out of n utterances, how many questions were found
    print(f"Found {len(host_questions)} interviewer questions out of {len(transcript.utterances)} utterances in {transcript.id}.\n")
    f.close()
# # print(f"Extracted a total of host {len(all_questions)} questions from {len(transcript_files[:1])} transcripts.")

