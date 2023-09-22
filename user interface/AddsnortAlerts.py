import requests
from web3 import Web3
import json
import time
from datetime import datetime

# Connect to the Ganache network
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load the ABI of the smart contract
with open("alerts_abi.json", "r") as abi_file:
    contract_abi = json.load(abi_file)

# Replace 'YOUR_CONTRACT_ADDRESS' with the actual address of your deployed contract
contract_address = '0x3bb0931e3a238B7580f349C109353C73db82547a'

# Load the contract using its ABI and address
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to fetch alerts from an external API and add them to the contract
def fetch_and_add_alerts(api_url):
    try:
        while True:
            response = requests.get(api_url)
            alerts_data = response.json()

            print(f"Fetched {len(alerts_data)} alerts from the API:")
            for alert in alerts_data:
                print(alert)

                add_alert(
                    parse_timestamp(alert['timestamp']),
                    alert['alertMessage'],
                    alert['alertType'],
                    int(alert['priority']),
                    alert['sourceIP'],
                    alert['destinationIP']
                )
                
                print("Alert added to Ganache network.")

            print("Alerts added successfully. Waiting for new alerts...")
            time.sleep(60)  # Fetch every minute

    except Exception as e:
        print("Error:", str(e))

# Function to parse the timestamp string into a datetime object
def parse_timestamp(timestamp_str):
    # Attempt to parse multiple timestamp formats
    for format_string in ["%m/%d-%H:%M:%S.%f", "%m/%d-%H:%M:%S"]:
        try:
            return datetime.strptime(timestamp_str, format_string)
        except ValueError:
            pass
    return None  # Return None if no valid format is found

# Add an alert to the contract
def add_alert(timestamp, alert_message, alert_type, priority, source_ip, destination_ip):
    if not web3.is_connected():
        print("Not connected to the Ethereum network.")
        return
    
    if not web3.eth.default_account:
        print("No Ethereum account is set.")
        return
    
    try:
        tx_hash = contract.functions.addAlert(
            int(timestamp.timestamp()),  # Convert datetime to Unix timestamp
            alertMessage,
            alertType,
            priority,
            sourceIP,
            destinationIP
        ).transact({
        'from': w3.eth.accounts[0],
        })
        
        tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print("Alert added. Transaction hash:", tx_hash.hex())
        print("Gas used:", tx_receipt['gasUsed'])
        
    except Exception as e:
        print("Error:", str(e))

# Example usage
if __name__ == "__main__":
    api_url = "http://localhost:3000/alerts"  # Replace with the actual API URL
    print(f"Fetching and adding alerts from {api_url}...")
    fetch_and_add_alerts(api_url)
