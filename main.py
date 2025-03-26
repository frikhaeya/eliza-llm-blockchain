import os
import requests
from dotenv import load_dotenv
from web3 import Web3, HTTPProvider
from eth_account import Account

# Suppress warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load environment variables
load_dotenv()
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")
SEPOLIA_API = os.getenv("SEPOLIA_API")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Setup Web3 with Alchemy
print(f"Connecting to Sepolia using: {SEPOLIA_API}")
provider = HTTPProvider(SEPOLIA_API, request_kwargs={"headers": {"Content-Type": "application/json"}})
w3 = Web3(provider)

def call_llm_api(user_input):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://eyafrikha.dev",
        "X-Title": "ElizaBot"
    }

    body = {
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

def send_transaction():
    try:
        print("🔁 Checking connection...")
        if not w3.is_connected():
            print("❌ Could not connect to Sepolia network")
            return

        nonce = w3.eth.get_transaction_count(PUBLIC_KEY)
        tx = {
            'nonce': nonce,
            'to': PUBLIC_KEY,  # just sending to self for test purposes
            'value': w3.to_wei(0.0001, 'ether'),
            'gas': 21000,
            'gasPrice': w3.to_wei('10', 'gwei'),
            'chainId': 11155111  # Sepolia
        }

        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        print(f"type of signed_tx: {type(signed_tx)}")
        print(f"signed_tx content: {signed_tx}")

        tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
        print(f"✅ Transaction sent: {w3.to_hex(tx_hash)}")

    except Exception as e:
        print(f"❌ Failed to send transaction: {e}")

print("Welcome to Eliza with LLM + Blockchain!")
print("Type 'send transaction' to test the full flow, or 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    if "send transaction" in user_input.lower():
        print("Calling the LLM...")
        response = call_llm_api(user_input)
        print("LLM:", response)
        print("\nSending transaction to Sepolia...")
        send_transaction()
    else:
        print("ELIZA: I'm not sure I understand you fully.")

