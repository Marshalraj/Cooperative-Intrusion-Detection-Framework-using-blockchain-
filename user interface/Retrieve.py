from web3 import Web3
import json
# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Load contract ABI
abi_file_path = r'C:\Users\marshall\Desktop\ids_cooperative\AlertsContracts.json'
with open(abi_file_path) as f:
    contract_abi = json.load(f)

# Contract address after deployment
contract_address = '0x3bb0931e3a238B7580f349C109353C73db82547a'

# Connect to the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)  # establish a connection to smart contract by c address & abi  

# Function to retrieve all alerts
def get_all_alerts():
    alerts = contract.functions.getAllAlerts().call()   # call method h=gets all alerts frm the contract 
    return alerts

# Retrieve all alerts from the contract
all_alerts = get_all_alerts()   #get_all_alerts functyion retreive allalerts frm contract  store it ina variable all_alerts 

# Print all retrieved alerts in a clean format
print("All Alerts:")
for index, alert in enumerate(all_alerts, start=1): # print results in for loop
    print(f"Alert {index}:")
    print("Severity:", alert[0])
    print("Alert:", alert[1])
    print("Source IP:", alert[2])
    print("Destination IP:", alert[3])
    print("Timestamp:", alert[4])
    print("Payload:", alert[5])
    print("Protocol:", alert[6])
    print("-" * 50)
