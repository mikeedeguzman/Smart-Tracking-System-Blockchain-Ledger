import time

import pandas as pd
from web3 import Web3


CSV_FILE = "MO-IT148 Homework_ IoT Data Simulation H3101 TEAM CTRL+ALT+ELITE ADET EDITION.csv"

GANACHE_URL = "http://127.0.0.1:7545"

# Replace this with the full deployed contract address copied from Remix.
CONTRACT_ADDRESS = "0x7457Ee1dE229eDfdc37a4f1CeCc1524cD1efa9d8"

ABI = [
    {
        "inputs": [
            {"internalType": "string", "name": "_deviceId", "type": "string"},
            {"internalType": "string", "name": "_dataType", "type": "string"},
            {"internalType": "string", "name": "_dataValue", "type": "string"},
        ],
        "name": "storeData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTotalRecords",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "index", "type": "uint256"}],
        "name": "getRecord",
        "outputs": [
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"internalType": "string", "name": "deviceId", "type": "string"},
            {"internalType": "string", "name": "dataType", "type": "string"},
            {"internalType": "string", "name": "dataValue", "type": "string"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]


def clean_value(value, fallback="N/A"):
    if pd.isna(value):
        return fallback
    return str(value)


def build_logistics_record(row):
    device_id = clean_value(row["Shipment_ID"])
    data_type = "Smart Logistics Tracking"

    data_value = (
        f"Event {clean_value(row['Event_ID'])} | "
        f"Checkpoint: {clean_value(row['Checkpoint'])} | "
        f"Status: {clean_value(row['Action_Type'])} | "
        f"Location: {clean_value(row['Latitude'])}, {clean_value(row['Longitude'])} | "
        f"Temp: {clean_value(row['Temperature_C'])} C | "
        f"Humidity: {clean_value(row['Humidity_%'])}% | "
        f"Shock: {clean_value(row['Shock_G-force'])} G | "
        f"Battery: {clean_value(row['Battery_%'])}% | "
        f"Signal: {clean_value(row['Network_Signal'])} | "
        f"Anomaly: {clean_value(row['Anomaly_Flag'], 'NORMAL')}"
    )

    return device_id, data_type, data_value


web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

if web3.is_connected():
    print("Connected to Ganache successfully!")
else:
    print("Connection failed. Ensure Ganache is running.")
    raise SystemExit

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)
web3.eth.default_account = web3.eth.accounts[0]

print(f"Connected to Smart Contract at {CONTRACT_ADDRESS}")
print(f"Default sender: {web3.eth.default_account}")

df = pd.read_csv(CSV_FILE)
print("CSV loaded successfully!")
print(df.head())

total_before = contract.functions.getTotalRecords().call()
print(f"Total records before upload: {total_before}")

available_slots = 100 - total_before
if len(df) > available_slots:
    raise ValueError(
        f"The contract only has {available_slots} available slots, "
        f"but the CSV has {len(df)} rows. Redeploy the contract or upload fewer rows."
    )

for index, row in df.iterrows():
    device_id, data_type, data_value = build_logistics_record(row)

    txn = contract.functions.storeData(device_id, data_type, data_value).transact({
        "from": web3.eth.default_account,
        "gas": 3000000,
    })

    receipt = web3.eth.wait_for_transaction_receipt(txn)
    print(
        f"Row {index + 1}/{len(df)} stored | "
        f"Shipment: {device_id} | "
        f"Txn Hash: {receipt.transactionHash.hex()}"
    )
    time.sleep(0.25)

total_after = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_after}")

first_record = contract.functions.getRecord(0).call()
print("First Stored Record:", first_record)

last_record = contract.functions.getRecord(total_after - 1).call()
print("Latest Stored Record:", last_record)
