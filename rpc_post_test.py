import requests
import json

url = "https://eth-sepolia.g.alchemy.com/v2/69t9sNLfdDgH0obsvgYGF5MyprQ6dn5kU"
headers = {"Content-Type": "application/json"}
payload = {
    "jsonrpc":"2.0",
    "method":"eth_blockNumber",
    "params":[],
    "id":1
}

try:
    response = requests.post(url, headers=headers, json=payload)
    print("✅ Status:", response.status_code)
    print("📦 Response:", response.json())
except Exception as e:
    print("❌ Error:", str(e))

