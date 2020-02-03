# DeltaKaggle Credit Applications
This web application is intended for a financial institution to facilitate the acceptance or denial of applications for credit. 
The front end user chooses numeric ranges within a number of variables dictated by a data set with over 100K credit applications. No names are included in the data set(acquired from a kaggle.com competition, now closed). The dataset is instead comprised of basic aspects of personal credit histories(info on delinquencies) and financial circumstances(age, income levels, and number of dependents). The results are returned to the user of the application with numeric ID's for each accepted applicant, as well as statistics related to the overall set of the accepted applications. 

## Getting Started
* Clone the github repo
* In the server directory, run:
  * `pipenv install`
* In the client directory, run:
  * `npm install`
  * `npm run build`
* Create a `.env` file in the project root with the following information:
```
APP_ID=deltakaggle
APP_SECRET=deltakaggle_secret
DB_URL=db_url
DB_NAME=db_name
DB_USER=db_username
DB_PASS=db_password
RUN_ENVIRONMENT=local
```
* Serve the application from `/server` with `pipenv run python main.py`
* Deltakaggle web interface will be available at https://localhost:5000/

## Prerequisites
* Node (>9.8.0)
* Web-browser (Chrome preferred, limited testing on alternative browsers)

## Built with:
* Python (Flask)
* Vue.js
* SQLite / PostgreSQL

## Author
Steve Porter

## License
This project is licensed under the [MIT License](LICENSE.md)

