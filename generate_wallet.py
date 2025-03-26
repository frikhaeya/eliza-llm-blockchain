from eth_account import Account

# Generate new Ethereum wallet (Goerli-compatible)
wallet = Account.create()

print("✅ Wallet generated")
print("Address:", wallet.address)
print("Private Key:", wallet.key.hex())

