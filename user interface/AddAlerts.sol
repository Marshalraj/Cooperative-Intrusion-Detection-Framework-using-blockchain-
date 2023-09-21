// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SnortAlerts {                // name of the contract 
    struct Alert {                    //structure of the alert messages 
        uint256 timestamp;
        string alertMessage;
        string sourceIP;
        string destinationIP;
        string alertType;
        uint8 priority;
    }

    Alert[] public alerts;         // alerts  array, named as public so, anyone can call this from outside 

    function addAlert(                    // function named addalert 
        uint256 timestamp,
        string memory alertMessage,        //stored in different locations, primarily in storage, memory, or stack
        string memory sourceIP,
        string memory destinationIP,
        string memory alertType,
        uint8 priority
    ) public {
        alerts.push(Alert({                   // push the alerts inmto the current array of alerts 
            timestamp: timestamp,
            alertMessage: alertMessage,
            sourceIP: sourceIP,
            destinationIP: destinationIP,
            alertType: alertType,
            priority: priority
        }));
    }

    function getAlertsCount() public view returns (uint256) {     ///// just simly display the count of the alerts inthe database... 
        return alerts.length;
    }

    function getAlert(uint256 index) public view returns (     // function to rtretrieve the alerts from tjhe database 
        uint256 timestamp,
        string memory alertMessage,
        string memory sourceIP,
        string memory destinationIP,
        string memory alertType,
        uint8 priority
    ) {
        require(index < alerts.length, "Index out of bounds");   // require fun validate the index with the no of  index in a arrary
        Alert memory alert = alerts[index];
        return (
            alert.timestamp, 
            alert.alertMessage,
            alert.sourceIP,
            alert.destinationIP,
            alert.alertType,
            alert.priority
        );
    }
}
