# ============================================================
# Deploy IoTDataStorage.sol to Ganache
#
# 1) Run this script (VSCode/terminal)
#    - pip install py-solc-x web3
#    - python deploy_contract.py
#    - prints the deployed contract address
#
# 2) Or just use Remix:
#    - paste IoTDataStorage.sol into remix.ethereum.org
#    - compile with solc 0.8.18
#    - Deploy & Run -> "Dev - Ganache Provider"
#      (or External HTTP Provider -> http://127.0.0.1:7545)
#    - deploy, then grab the address from "Deployed Contracts"
#
# Either way: copy the resulting address into CONTRACT_ADDRESS
# in week5_milestone1_submission.py and week6_data_retrieval.py
# ============================================================

from solcx import compile_source, install_solc, set_solc_version
from web3 import Web3

GANACHE_URL = "http://127.0.0.1:7545"
CONTRACT_FILE = "IoTDataStorage.sol"

# Install and select the Solidity compiler version matching the pragma
install_solc("0.8.18")
set_solc_version("0.8.18")

# Read the contract source
with open(CONTRACT_FILE, "r") as f:
    source_code = f.read()

# Compile
compiled = compile_source(source_code, output_values=["abi", "bin"])
contract_id, contract_interface = compiled.popitem()

abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))
if not web3.is_connected():
    print("Connection failed. Ensure Ganache is running.")
    raise SystemExit

web3.eth.default_account = web3.eth.accounts[0]
print(f"Deploying from: {web3.eth.default_account}")

# Deploy
Contract = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Contract.constructor().transact({"from": web3.eth.default_account, "gas": 3000000})
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"\n✅ Contract deployed successfully!")
print(f"Contract Address: {contract_address}")
print(f"\nCopy this address into CONTRACT_ADDRESS in your week5/week6 scripts.")

# Save ABI to file for reference (optional)
import json
with open("contract_abi.json", "w") as f:
    json.dump(abi, f, indent=2)
print("ABI also saved to contract_abi.json")