from sql_alchemy_db_instance import db
from sqlalchemy import Column, Integer, Float

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

