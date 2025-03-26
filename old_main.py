import os
import requests
from dotenv import load_dotenv

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Load your .env file
load_dotenv()

def call_llm_api(user_input):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://eyafrikha.dev",  # can be anything
        "X-Title": "ElizaBot"
    }

    body = {
        # "model": "openai/gpt-3.5-turbo",
        # "model": "openrouter/cinematika-7b",
        "model": "mistralai/mistral-small-3.1-24b-instruct:free",
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body, verify=False)
        if res.status_code == 200:
            return res.json()['choices'][0]['message']['content']
        else:
            return f"Error {res.status_code}: {res.text}"
    except Exception as e:
        return f"Exception: {str(e)}"

# Simple conversation loop
print("Welcome to Eliza with LLM! Type 'send transaction' to test the API or 'exit' to quit.")
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    elif "send transaction" in user_input.lower():
        print("Calling the LLM...")
        response = call_llm_api(user_input)
        print("LLM:", response)

    else:
        print("ELIZA: I'm not sure I understand you fully.")  # Placeholder

