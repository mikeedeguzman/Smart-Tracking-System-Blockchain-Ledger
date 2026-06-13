import pandas as pd
import numpy as np
from web3 import Web3

# Configuration
GANACHE_URL = "http://127.0.0.1:7545"
CONTRACT_ADDRESS = "0xAF5D8457982f15462235ADa59BF7a5d97a7D022C"

# ABI is required to interact with the contract
ABI = [
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

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))
if not web3.is_connected():
    print("Connection failed. Ensure Ganache is running.")
    raise SystemExit

contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=ABI)

# Retrieve total number of stored records
total_records = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_records}")

# Fetch all stored IoT data
data = []
for i in range(total_records):
    record = contract.functions.getRecord(i).call()
    data.append({
        "timestamp": record[0],
        "device_id": record[1],
        "data_type": record[2],
        "data_value": record[3]
    })

# Convert to a DataFrame
df = pd.DataFrame(data)

# Convert timestamp to readable format
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")

# Clean data: Extract numeric values from 'data_value'
# The data_value contains mixed formats, e.g., "Temp: 22.5 C | Humidity: 50%"
# Extracting the first floating point number found
df["numeric_value"] = df["data_value"].str.extract(r'(\d+\.?\d*)').astype(float)

# Handle missing values
df.fillna(0, inplace=True)

# Display cleaned data
print(df.head())

# Save cleaned IoT data to a CSV file
df.to_csv("cleaned_iot_data.csv", index=False)
print("✅ Cleaned IoT data saved successfully as cleaned_iot_data.csv")
