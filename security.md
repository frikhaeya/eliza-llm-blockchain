Theoretical Questions – Munich RE Coding Challenge

1. Potential Security Issues
Exposing private keys: Hardcoding or committing private keys can lead to unauthorized transactions or fund theft.

Unfiltered LLM output triggering transactions: The agent may generate unintended or malicious actions.

Lack of limits on transaction value: The system could unknowingly send large amounts of cryptocurrency.

Overuse of testnet/mainnet RPC endpoints: Risk of rate-limiting or abuse if left unprotected.

2. Mitigation Strategies
Secure secret management: Use .env files and avoid committing them to version control. Consider secret managers for production.

Restrict LLM capabilities: Whitelist only safe commands (e.g., trigger transaction only on exact match like "send transaction").

Enforce transaction limits: Limit how much can be sent per transaction and per session.

Testnet-only policy for development: Always use testnets (e.g., Sepolia) when working with LLM-controlled agents.
