from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
rpc_url = os.getenv("SEPOLIA_API")
w3 = Web3(Web3.HTTPProvider(rpc_url))

print("Connected:", w3.is_connected())

