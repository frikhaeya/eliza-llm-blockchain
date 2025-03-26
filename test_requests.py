import requests

try:
    res = requests.get("https://api.openai.com")
    print("✅ HTTPS request worked.")
except Exception as e:
    print("❌ HTTPS error:", e)

