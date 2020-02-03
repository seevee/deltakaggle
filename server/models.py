from sql_alchemy_db_instance import db
import pandas as pd
import sqlite3
from sqlalchemy import Column, Integer, Float
import pandas as pd
import numpy as np
from pandas import DataFrame
from flask_sqlalchemy import SQLAlchemy

class Variables(db.Model):

    __tablename__ = 'APPLICANTS'
    id = db.Column(db.Integer, primary_key=True)
    SeriousDlqin2yrs =  db.Column(db.Integer)
    RevolvingUtilizationOfUnsecuredLines = db.Column(db.Float)
    age = db.Column(db.Integer)
    NumberOfTime30to59DaysPastDueNotWorse = db.Column(db.Integer)
    DebtRatio = db.Column(db.Float)
    MonthlyIncome = db.Column(db.Integer)
    NumberOfOpenCreditLinesAndLoans = db.Column(db.Integer)
    NumberOfTimes90DaysLate = db.Column(db.Integer)
    NumberRealEstateLoansOrLines = db.Column(db.Integer)
    NumberOfTime60to89DaysPastDueNotWorse = db.Column(db.Integer)
    NumberOfDependents = db.Column(db.Integer)

