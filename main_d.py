import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
print("Loaded API Key:", api_key[:8], "..." if api_key else "❌ NOT FOUND")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://example.com",
    "X-Title": "TestBot"
}

body = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say hi!"}]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

print("Status:", response.status_code)
print("Response:", response.text)

