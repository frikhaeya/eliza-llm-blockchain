from web3 import Web3

url = "https://eth-sepolia.g.alchemy.com/v2/69t9sNLfdDgH0obsvgYGF5MyprQ6dn5kU"
w3 = Web3(Web3.HTTPProvider(url))

try:
    latest_block = w3.eth.block_number
    print("✅ Latest block:", latest_block)
except Exception as e:
    print("❌ Error:", str(e))

