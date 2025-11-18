import requests
from dotenv import load_dotenv
import os

class AssemblyAI_API:
    BASE_URL = "https://api.assemblyai.com/"

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('ASSEMBLYAI_APIKEY')
        self.headers = {
            "authorization": self.api_key,
            "content-type": "application/json"
        }

    def transcribe_audio(self, audio_url):
        endpoint = self.BASE_URL + "/v2/transcript"
        payload = {
            "audio_url": audio_url,
            "audio_end_at": None,
            "audio_start_from": 10,
            "auto_chapters": True,
            "auto_highlights": False,
            "content_safety": False,
            "disfluencies": False,
            "entity_detection": False,
            "filter_profanity": False,
            "format_text": True,
            "iab_categories": False,
            "language_code": "en_us",
            "language_confidence_threshold": 0.7,
            "language_detection": False,
            "multichannel": False,
            "punctuate": True,
            "redact_pii_sub": "hash",
            "sentiment_analysis": False,
            "speaker_labels": True,
            "summarization": False,
                    }
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)

        except requests.RequestException as e:
            code = response.status_code
            if code == 400:
                raise ValueError(f"Bad Request (400): Check your payload or audio_url. {response.error}")
            elif code == 401:
                raise PermissionError(f"Unauthorized (401): Invalid or missing API key. {response.error}")
            elif code == 404:
                raise FileNotFoundError(f"Not Found (404): The requested resource does not exist. {response.error}")
            elif code == 429:
                raise RuntimeError(f"Too Many Requests (429): Rate limit exceeded, retry later. {response.error}")
            elif code == 500:
                raise RuntimeError(f"Internal Server Error (500): AssemblyAI had an internal issue. {response.error}")
            elif code == 503:
                raise RuntimeError(f"Service Unavailable (503): AssemblyAI temporarily down, retry later. {response.error}")
            elif code == 504:
                raise TimeoutError(f"Gateway Timeout (504): AssemblyAI timed out processing your request. {response.error}")
            elif code != 200:
                raise RuntimeError(f"Unexpected status {code}: {response.error}")
            print(f"Error during AssemblyAI transcription request: {e}")
            return None
        # If status code is 200, return JSON response
        return response.json()

    def list_transcripts(self):
        endpoint = self.BASE_URL + "/v2/transcript?" + "status=completed&limit=200"
        transcripts_list = []
        response = requests.get(endpoint, headers=self.headers)
        if response.status_code == 200:
            transcripts_list = response.json().get('transcripts', [])
        else:
            print(f"Error fetching transcripts: {response.status_code} {response.text}")
        return transcripts_list
    def delete_transcript(self, transcript_id):
        endpoint = self.BASE_URL + "/v2/transcript/" + transcript_id
        
        response = requests.delete(endpoint, headers=self.headers)
        if response.status_code == 200:
            print(f"Deleted transcript {transcript_id} successfully.")
        else:
            print(f"Error deleting transcript {transcript_id}: {response.status_code} {response.text}")
        return response
    def get_transcript(self, transcript_id):
        endpoint = self.BASE_URL + "/v2/transcript/" + transcript_id
        
        response = requests.get(endpoint, headers=self.headers).json()
        return response