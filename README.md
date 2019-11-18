DeltaKaggle Credit Applications

This web application is intended for a financial institution to facilitate the acceptance or denial of applications for credit. 
From a kaggle.com competition, now closed, it selects for acceptance from a data set comprised of over 100K individual 
consumer financial reports, based on the variable ranges chosen by the user. No names are included in the data set, 
it is instead comprised of basic aspects of personal credit history. The results are returned to the user of application with numeric
ID's for each accepted applicant, as well as statisitics related to the overall set of the accepted applications. 

Getting Started

Fork the github repo

In the server directory, run the following scripts
'pipenv install'
'pipenv install pandas'

In the client directory, run the following scripts
'npm intall'
'npm run build'

Create a .env file with the following information --> NOTE: the file should literally be titled '.env'

The information in this file with facilitate configuration for the DB instance

APP_ID = 'insert your data'
APP_SECRET = 'insert your data'
DB_LOCATION = 'insert your data'
DB_USERNAME = 'insert your data'
DB_PASS = 'insert your data'
CALLBACK_URL = 'insert your data'

To run the program on your local host(https://localhost:5000/) switch back to server directory and run

'pipenv run python main.py'

Prerequisites
What things you need to install the software and how to install them

Node (>9.8.0)
Web-browser (Chrome preferred, limited testing on alternative browsers)

Built with:

Python Flask
Vue.js
MySql

License
This project is licensed under the MIT License - see the LICENSE.md file for details

