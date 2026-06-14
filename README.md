# MO-IT148 Week 7: Data Visualization

**Section:** H3101
**Team:** TEAM CTRL+ALT+ELITE ADET EDITION

This project visualizes the preprocessed smart logistics IoT data retrieved from the local Ethereum blockchain (Ganache) in Week 6, using a line plot to show trends in sensor readings over time, grouped by device.

## Files
- `IoTDataStorage.sol` - Solidity smart contract deployed through Remix IDE.
- `week5_milestone1_submission.py` - Python script that reads the CSV and submits each row to the blockchain (Milestone 1 output).
- `week6_data_retrieval.py` - Python script that retrieves all stored records from the blockchain, processes them, and exports `cleaned_iot_data.csv`.
- `week7_visualization.py` - Python script that loads `cleaned_iot_data.csv` and generates a line plot of IoT data trends over time.
- `cleaned_iot_data.csv` - Cleaned and structured IoT data retrieved from the blockchain (input for Week 7).
- `MO-IT148 Homework_ IoT Data Simulation H3101 TEAM CTRL+ALT+ELITE ADET EDITION.csv` - Simulated smart logistics IoT dataset containing 80 records.

## Setup
1. Ensure `cleaned_iot_data.csv` exists (generated from `week6_data_retrieval.py`).
2. Install dependencies:
```bash
pip install pandas matplotlib seaborn
```
3. Run:
```bash
python week7_visualization.py
```

## Process Overview
1. **Access preprocessed data** from the Week 6 output:
```python
df = pd.read_csv("cleaned_iot_data.csv")
print(df.head())
```
2. **Convert timestamp to datetime** for proper plotting:
```python
df["timestamp"] = pd.to_datetime(df["timestamp"])
```
3. **Set visualization style:**
```python
sns.set_style("whitegrid")
```
4. **Create the line plot**, grouped by `device_id` to show trends per shipment:
```python
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["timestamp"], y=df["numeric_value"],
             hue=df["device_id"], marker="o")

plt.xticks(rotation=45)

plt.title("IoT Data Trends Over Time", fontsize=14)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Numeric Value", fontsize=12)

plt.legend(title="Device ID", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
```

## Notes
- The original instructions group the line plot by `data_type`. Since all retrieved records share the same `data_type` ("Smart Logistics Tracking"), the plot was instead grouped by `device_id` (Shipment ID) for more meaningful comparison across shipments.
- `numeric_value` corresponds to the first numeric value extracted from each record's `data_value` field during Week 6 preprocessing.

## Recorded Output
- Input file: `cleaned_iot_data.csv`
- Total records visualized: `80`
- Output: Line plot of `numeric_value` over `timestamp`, grouped by `device_id`

## Remarks
This repository contains the Week 7 project output of TEAM CTRL+ALT+ELITE ADET EDITION for MO-IT148. The visualization is based on the 80 IoT data entries retrieved from the team's local Ganache blockchain in Week 6.
