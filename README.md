# MO-IT148 Milestone 1: Smart Tracking System Blockchain Ledger

**Section:** H3101  
**Team:** TEAM CTRL+ALT+ELITE ADET EDITION

This project stores simulated smart logistics IoT records on a local Ethereum blockchain using Ganache, Remix IDE, Solidity, Python, pandas, and Web3.py.

## Files

- `IoTDataStorage.sol` - Solidity smart contract deployed through Remix IDE.
- `week5_milestone1_submission.py` - Python script that reads the CSV and submits each row to the blockchain.
- `MO-IT148 Homework_ IoT Data Simulation H3101 TEAM CTRL+ALT+ELITE ADET EDITION.csv` - Simulated smart logistics IoT dataset containing 80 records.
- `milestone1_worksheet_answers.md` - Verified worksheet values for the Milestone 1 submission.

## Setup

1. Open Ganache and confirm the RPC server is `http://127.0.0.1:7545`.
2. Deploy `IoTDataStorage.sol` in Remix using Solidity `0.8.18` and the External HTTP Provider.
3. Install dependencies:

```bash
pip install pandas web3
```

4. Update `CONTRACT_ADDRESS` in the Python script if a new contract is deployed.
5. Run:

```bash
python week5_milestone1_submission.py
```

## Recorded Submission Output

- Contract address: `0xAF5D8457982f15462235ADa59BF7a5d97a7D022C`
- Ganache RPC server: `http://127.0.0.1:7545`
- Records already present before CSV upload: `2`
- CSV records uploaded successfully: `80`
- Total records after upload: `82`
- First CSV transaction hash: `0x5f11799784fe79802dcaae14e4bcd397a62bdbaa4608b6f1e7e15c2d8159b6fa`
- Last CSV transaction hash: `0x042685ec0f55f00466b3ebbb374f2565e34adf75a8a3d41336a432ad39fc94d6`

The two records already present were manual Remix test records. Adding the 80 CSV rows resulted in 82 total records stored on the blockchain.

## Important Note

Do not run the full upload script again against the same deployed contract. The smart contract has a maximum capacity of `100` records, and rerunning the script would create duplicate entries until the limit is reached.
