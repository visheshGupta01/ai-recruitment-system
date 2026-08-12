import requests


# Hugging Face Inference API URL for embeddings
API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

def get_embedding(text):
    response = requests.post(
        API_URL, headers=headers, json={
            "inputs": text, "options": {"wait_for_model": True}}
    )
    return response.json()


def create_embedding(text):
    return get_embedding(text)