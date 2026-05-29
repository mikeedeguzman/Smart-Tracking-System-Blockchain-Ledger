# MO-IT148 Milestone 1: Smart Tracking System Blockchain Ledger (Submission) H3101 TEAM CTRL+ALT+ELITE ADET EDITION

## GitHub Link

GitHub Link: https://github.com/jenncar77/MO-IT148-Smart-Tracking-System-Blockchain-Ledger-TEAM-CTRL-ALT-ELITE-ADET-EDITION

## Setting Up The Environment

Was your connection successful? Yes

If No, describe the error and how you fixed it:
Not applicable. The connection to Ganache was successful using the RPC server `http://127.0.0.1:7545`.

Screenshot to attach:
Console output showing `Connected to Ganache successfully!`

## Smart Contract Interaction

Smart Contract Address:
0xAF5D8457982f15462235ADa59BF7a5d97a7D022C

Total Records Before Storing Data:
2

Did you encounter any errors while loading the contract? No

If Yes, describe how you fixed it:
Not applicable. The smart contract was successfully loaded in Python using Web3.py.

Screenshot to attach:
Console output confirming connection to the smart contract.

## Storing IoT Data On The Blockchain

Number of records in CSV file:
80

First three records in CSV:

1. Event 1, Shipment ID: PH-DAV-2026-0001, Checkpoint: WAREHOUSE_PICKUP, Action: PICKUP, Location: 13.462483, 123.262439, Temperature: 6.8 C, Signal: NONE, Anomaly: CONNECTION_LOST
2. Event 2, Shipment ID: PH-DAV-2026-0001, Checkpoint: SLEX_TOLL, Action: TOLL_PASS, Location: 13.335912, 123.301817, Temperature: 10.0 C, Signal: GOOD, Anomaly: NORMAL
3. Event 3, Shipment ID: PH-DAV-2026-0001, Checkpoint: RIDER_HANDHELD, Action: ASSIGN, Location: 13.387291, 123.305393, Temperature: 10.2 C, Signal: NONE, Anomaly: CONNECTION_LOST

Screenshot to attach:
Console output showing the CSV preview from Python.

Number of records successfully stored on blockchain:
80

Transaction Hash of first stored record:
5f11799784fe79802dcaae14e4bcd397a62bdbaa4608b6f1e7e15c2d8159b6fa

Transaction Hash of last stored record:
042685ec0f55f00466b3ebbb374f2565e34adf75a8a3d41336a432ad39fc94d6

Screenshot to attach:
Console output showing successful row-by-row transactions.

## Retrieving & Verifying Data

Total records now stored on blockchain:
82

First stored record retrieved from blockchain:

Timestamp:
1780080086

Device ID:
PKG001

Data Type:
Location

Data Value:
Manila Warehouse

Screenshot to attach:
Console output showing retrieved records from `getRecord(0)` and the latest stored record.

Latest stored record retrieved from blockchain:

Timestamp:
1780083547

Device ID:
PH-MAN-2026-0020

Data Type:
Smart Logistics Tracking

Data Value:
Event 80 | Checkpoint: DOORSTEP_ePOD | Status: DELIVERY | Location: 14.62198, 121.047597 | Temp: 6.0 C | Humidity: 74.6% | Shock: 0.21 G | Battery: 83% | Signal: EXCELLENT | Anomaly: NORMAL

## Notes

The total record count is 82 because the smart contract already had 2 manual test records before uploading the 80 CSV records. If a clean total of 80 is required, redeploy the smart contract in Remix, copy the new contract address, and run the Week 5 Python script again.
