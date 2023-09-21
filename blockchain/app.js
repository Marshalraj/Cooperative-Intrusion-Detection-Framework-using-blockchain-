const express = require('express');
const fs = require('fs/promises'); // File system module with promises
const cors = require('cors'); // Import the cors package

const app = express();
const PORT = process.env.PORT || 3000;
const ALERTS_FILE = 'etc/log/snort/alerts.txt'; // Change this to your ASCII text file name

app.use(express.json());

// Use the cors middleware
app.use(cors());

app.get('/alerts', async (req, res) => {      //http het request/(code for reading and responding with alerts)
  try {
    const alertsData = await fs.readFile(ALERTS_FILE, 'utf8');    //reading the alert file ehich is utf8 encoding 
    const alertsArray = alertsData.split('\n'); // Split alerts into an array

      const alerts = alertsArray.map(alertLine => {          //alertsArray is an array containing individual lines of text/map high order to iterate 
      const match = alertLine.match(/^(.*?) \[.*?\] \[.*?\] (.*?) \[Classification: (.*?)\] \[Priority: (\d+)\] {.*} (.*?) -> (.*?)$/); //
      if (!match) return null;

      const [, timestamp, alertMessage, alertType, priority, sourceIP, destinationIP] = match;  // it look for the strings in the array to match
      return { 
        timestamp,
        alertMessage,
        alertType,
        priority,
        sourceIP,
        destinationIP,
      };
    }).filter(alert => alert !== null); //this filter fun remove all null values 

    res.json(alerts); //once all parsed, then respond  json to the client/ ir converts the array into json
  } catch (error) {       // it is a try ..catch block caught all error while parsing
      console.error('Error reading alerts file:', error);  //caught all error while parsing
    res.status(500).json({ error: 'Internal Server Error' }); // repomd to client if incase any error ' internal server error '
  } 
});

app.listen(PORT, () => {      // app refers to express, mention earlier in codee
  console.log(`Server is running on port ${PORT}`);  // server is running on port 3000
});
