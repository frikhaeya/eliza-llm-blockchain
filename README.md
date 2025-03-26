# Eliza + LLM + Blockchain Transaction (Sepolia Testnet)

This project is a solution to the **Munich RE coding challenge**, where the goal was to integrate the [Eliza](https://github.com/elizaOS/eliza) chatbot with a **Large Language Model (LLM)** and enable it to trigger a blockchain transaction.

The implemented system allows Eliza to respond intelligently via LLM, and on command, initiate a blockchain transaction on the **Ethereum Sepolia testnet**.

---

## Features

- Integration of Eliza chatbot with an LLM using [OpenRouter](https://openrouter.ai/)
- Blockchain transaction execution using [Web3.py](https://web3py.readthedocs.io/en/stable/)
- Transaction is triggered via a natural language command
- Supports Sepolia testnet via Infura RPC endpoint

---

## Tech Stack

- Python 3.10
- [OpenRouter API](https://openrouter.ai/) (free LLM API)
- `web3.py`
- Ethereum Sepolia testnet
- Infura for RPC access
- `dotenv` for environment variable management

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/frikhaeya/eliza-llm-blockchain.git
cd eliza-llm-blockchain
```

### 2. Create a .env File

Copy the example and fill in your own keys:

```bash
cp .env.example .env
```

Update the .env file with your keys:

```bash
OPENROUTER_API_KEY=your_openrouter_api_key
SEPOLIA_API=https://sepolia.infura.io/v3/your_infura_project_id
PRIVATE_KEY=your_private_key
PUBLIC_KEY=your_public_address
```

### 3. Set Up Python Environment

Create a virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4.  Run the Application

```bash
python3 main.py
```

You will be prompted by Eliza. Type:

```bash
send transaction
```

This will trigger the LLM, and if configured correctly, send a transaction on Sepolia.

### Output Example

You should see output similar to:

```yaml
LLM: Sending a transaction typically refers to transferring assets...
Connecting to Sepolia using: https://sepolia.infura.io/v3/your_project_id
Transaction sent: 0xabc123...def456
```
