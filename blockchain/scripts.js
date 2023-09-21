const alertsData = document.getElementById('alerts-data'); //get html element with id alerts-data and asiignto alertsdata

fetch('http://localhost:3000/alerts') //initiated  get request from the http server
  .then(response => response.json()) // app.js send json format to as response
  .then(alerts => {  //once json obtained,  it s a array of  object
    alerts.forEach(alert => {
      const row = document.createElement('tr'); // for each object in array, creates a new table row
      row.innerHTML =   // it insert   all the elements inot a array of table 
        <td class="timestamp">${alert.timestamp}</td>
        <td>${alert.alertMessage}</td>
        <td>${alert.sourceIP}</td>
        <td>${alert.destinationIP}</td>
        <td>${alert.alertType}</td>
        <td class="priority ${alert.priority.toLowerCase()}">${alert.priority}</td>
      `;
      alertsData.appendChild(row);   // After setting the content of the table row, it appends the row to the alertsData 
    });
  })
  .catch(error => console.error('Error fetching alerts:', error)); // After setting the content of the table row, it appends the row to the alertsData incase of error

