# DeltaKaggle Credit Applications

This web application is intended for a financial institution to facilitate the acceptance or denial of applications for credit. 
The front end user chooses numeric ranges within a number of variables dictated by a data set with over 100K credit applications. No names are included in the data set(acquired from a kaggle.com competition, now closed). The dataset is instead comprised of basic aspects of personal credit histories(info on delinquencies) and financial circumstances(age, income levels, and number of dependents). The results are returned to the user of the application with numeric ID's for each accepted applicant, as well as statistics related to the overall set of the accepted applications. 

## Getting Started

Fork the github repo

In the server directory, run the following scripts

`pipenv install`

In the client directory, run the following scripts

`npm install`

`npm run build`

Create a .env file with the following information --> NOTE: the file should literally be titled `.env`

The information in this file with facilitate configuration for the DB instance

APP_ID = 'insert your data'
APP_SECRET = 'insert your data'
DB_URL = 'insert your data'
DB_NAME = 'insert your data'
DB_USER = 'insert your data'
DB_PASS = 'insert your data'

To run the program on your local host(https://localhost:5000/) switch back to server directory and run

`pipenv run python main.py`

## Prerequisites
What things you need to install the software and how to install them

Node (>9.8.0)
Web-browser (Chrome preferred, limited testing on alternative browsers)

## Built with:
Python Flask
Vue.js
MySql

## Author
Steve Porter

## License
This project is licensed under the MIT License - see the LICENSE.md file for details


