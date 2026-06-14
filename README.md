MO-IT148 Week 6: Data Retrieval and Processing

**Section:** H3101
**Team:** TEAM CTRL+ALT+ELITE ADET EDITION

This project retrieves the simulated smart logistics IoT records previously stored on a local Ethereum blockchain (Ganache) in Milestone 1, structures the data using pandas, cleans it for analysis, and exports it as a CSV file.

## Files
- `IoTDataStorage.sol` - Solidity smart contract deployed through Remix IDE.
- `week5_milestone1_submission.py` - Python script that reads the CSV and submits each row to the blockchain (Milestone 1 output).
- `week6_data_retrieval.py` - Python script that retrieves all stored records from the blockchain, processes them, and exports `cleaned_iot_data.csv`.
- `cleaned_iot_data.csv` - Cleaned and structured IoT data retrieved from the blockchain.
- `MO-IT148 Homework_ IoT Data Simulation H3101 TEAM CTRL+ALT+ELITE ADET EDITION.csv` - Simulated smart logistics IoT dataset containing 80 records.

## Setup
1. Open Ganache and confirm the RPC server is `http://127.0.0.1:7545`.
2. Ensure `IoTDataStorage.sol` is deployed (the same contract used for Milestone 1 submission) and that `CONTRACT_ADDRESS` in `week6_data_retrieval.py` matches the deployed address.
3. Install dependencies:
```bash
pip install pandas numpy web3
```
4. Run:
```bash
python week6_data_retrieval.py
```

## Process Overview
1. **Retrieve Milestone 1 output** - Connects to the same deployed contract used to store the 80 IoT records.
2. **Get total records:**
```python
total_records = contract.functions.getTotalRecords().call()
print(f"Total IoT records stored: {total_records}")
```
3. **Fetch and structure data into a DataFrame:**
```python
data = []
for i in range(total_records):
    record = contract.functions.getRecord(i).call()
    data.append({
        "timestamp": record[0],
        "device_id": record[1],
        "data_type": record[2],
        "data_value": record[3]
    })

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
print(df.head())
```
4. **Preprocess for analysis:**
   - Extract numeric values from `data_value` (mixed text/units, e.g. "Temp: 22.5 C | Humidity: 50%").
   - Handle missing values by replacing them with `0`.
```python
df["numeric_value"] = df["data_value"].str.extract(r'(\d+\.?\d*)').astype(float)
df.fillna(0, inplace=True)
print(df.head())
```
5. **Save cleaned data to CSV:**
```python
df.to_csv("cleaned_iot_data.csv", index=False)
print("✅ Cleaned IoT data saved successfully as cleaned_iot_data.csv")
```

## Recorded Retrieval Output
- Contract address: `0x7457Ee1dE229eDfdc37a4f1CeCc1524cD1efa9d8`
- Ganache RPC server: `http://127.0.0.1:7545`
- Total records retrieved from blockchain: `80`
- Output file: `cleaned_iot_data.csv`

## Remarks
This repository contains the Week 6 project output of TEAM CTRL+ALT+ELITE ADET EDITION for MO-IT148. The retrieved records correspond to the 80 IoT data entries uploaded to the smart contract during the Milestone 1 submission, read directly from the team's local Ganache blockchain.
