import json

from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Load contract ABI
abi_file_path = r'C:\Users\marshall\Desktop\ids_cooperative\AlertsContracts.json'
with open(abi_file_path) as f:
    contract_abi = json.load(f)['abi']

# Contract address after deployment
contract_address = '0x3bb0931e3a238B7580f349C109353C73db82547a'

# Connect to the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Function to add an alert
def add_alert(alert_data):
    tx_hash = contract.functions.addAlert(
        alert_data['Severity'],
        alert_data['Alert'],
        alert_data['Source IP'],
        alert_data['Destination IP'],
        alert_data['Timestamp'],
        alert_data['Payload'],
        alert_data['Protocol']
    ).transact({
        'from': w3.eth.accounts[0],
    })

    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction hash:", tx_hash.hex())
    print("Alert added successfully.")

# List of example alert data
alerts_to_add = [
    {
        "Severity": "High",
        "Alert": "Attempted User Privilege Gain",
        "Source IP": "192.168.1.100",
        "Destination IP": "10.0.0.1",
        "Timestamp": "2023-07-28 12:34:56",
        "Payload": "abcdef1234567890",
        "Protocol": "TCP",
    },
       {
        "Severity": "Low",
        "Alert": "Informational Alert",
        "Source IP": "192.168.1.102",
        "Destination IP": "10.0.0.3",
        "Timestamp": "2023-07-28 15:20:10",
        "Payload": "a1b2c3d4e5f6",
        "Protocol": "HTTP"
    },
     {
        "Severity": "High",
        "Alert": "Attempted User Privilege Gain",
        "Source IP": "192.168.1.100",
        "Destination IP": "10.0.0.1",
        "Timestamp": "2023-07-28 12:34:56",
        "Payload": "abcdef1234567890",
        "Protocol": "TCP"
    },
    {
        "Severity": "Medium",
        "Alert": "Unauthorized Access Detected",
        "Source IP": "192.168.1.101",
        "Destination IP": "10.0.0.2",
        "Timestamp": "2023-07-28 13:45:23",
        "Payload": "1234567890abcdef",
        "Protocol": "UDP"
    },
     {
        "Severity": "High",
        "Alert": "Attempted User Privilege Gain",
        "Source IP": "192.168.1.100",
        "Destination IP": "10.0.0.1",
        "Timestamp": "2023-07-28 12:34:56",
        "Payload": "abcdef1234567890",
        "Protocol": "TCP"
    },
    {
        "Severity": "Medium",
        "Alert": "Unauthorized Access Detected",
        "Source IP": "192.168.1.101",
        "Destination IP": "10.0.0.2",
        "Timestamp": "2023-07-28 13:45:23",
        "Payload": "1234567890abcdef",
        "Protocol": "UDP"
    },
    {
        "Severity": "Low",
        "Alert": "Informational Alert",
        "Source IP": "192.168.1.102",
        "Destination IP": "10.0.0.3",
        "Timestamp": "2023-07-28 15:20:10",
        "Payload": "a1b2c3d4e5f6",
        "Protocol": "HTTP"
    },
    {
        "Severity": "High",
        "Alert": "Malware Detected",
        "Source IP": "192.168.1.105",
        "Destination IP": "10.0.0.6",
        "Timestamp": "2023-07-29 08:12:34",
        "Payload": "f6e5d4c3b2a1",
        "Protocol": "SMTP"
    }

    # Add more alerts here...
]

# Add each alert to the contract
for alert_data in alerts_to_add:
    add_alert(alert_data)
