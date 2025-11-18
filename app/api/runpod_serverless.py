from dotenv import load_dotenv
import requests
import os
import json

class infinity_embeddings:
    def __init__(self, model):
        load_dotenv()
        self.model = model
        self.API_KEY = os.getenv("RUNPOD_API_EMBEDDINGS")
        self.url = "https://api.runpod.ai/v2/lhc96ll22wg25g/openai/v1/embeddings"
    def get_embeddings(self, input):
        print("HERE")
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.API_KEY}" 
        }

        data = {
            'model': self.model,
            'input': input
        }
        try:
            response = requests.post(self.url, headers=headers, json=data)
            payload = response.content 
            payload_json = json.loads(payload.decode())
            emb_blocks = payload_json["data"]
            total_tokens = payload_json["usage"]["total_tokens"]

            embeddings = [elem["embedding"] for elem in emb_blocks]
            # print(embeddings)
            response = {
                "embeddings": embeddings,
                "total_tokens": total_tokens
            }
            return response 
        except Exception as e:
            print(f"Error in request: {e}")