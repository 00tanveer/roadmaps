# Load the transcript object into memory and study them
from app.models.transcript import Transcript
import json 
import os
from pydantic import ValidationError

# get all transcript json filepaths in directory data/transcripts/
transcript_files = os.listdir("data/transcripts/")
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