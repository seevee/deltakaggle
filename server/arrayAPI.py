from flask import Blueprint, jsonify, request
import pandas as pd
import numpy as np
import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from pandas import DataFrame
import sqlite3
from models import Variables
from sql_alchemy_db_instance import db
from sqlalchemy.sql import func

"""
app does not clear accepted applicants at refresh of browser
"""

array_api = Blueprint('array_api', __name__)

eligible_applicants = []
statistics = []


@array_api.route('/user_vars', methods=['GET', 'POST'])
def serve_user_vars():

    entered_age = request.json["age_item"]
    entered_income = request.json["income_item"]
    entered_util = request.json["util_item"]
    entered_thirtysixty = request.json["thirtysixty_item"]
    entered_debtratio = request.json["debtratio_item"]
    entered_minopenlines = request.json["minlines_item"]
    entered_ninety = request.json["ninety_item"]
    entered_realestate = request.json["realestate_item"]
    entered_sixtyninety = request.json["sixtyninety_item"]
    entered_dependents = request.json["dependents_item"]

    variable_instances = db.session.query(Variables).filter(Variables.age >= entered_age[0], Variables.age <= entered_age[1],
                            Variables.MonthlyIncome >= entered_income[0], Variables.RevolvingUtilizationOfUnsecuredLines <= entered_util[0],
                            Variables.NumberOfTime30to59DaysPastDueNotWorse <= entered_thirtysixty[0], Variables.DebtRatio <= entered_debtratio[0],
                            Variables.NumberOfOpenCreditLinesAndLoans >= entered_minopenlines[0], Variables.NumberOfTimes90DaysLate <= entered_ninety[0],
                            Variables.NumberRealEstateLoansOrLines >= entered_realestate[0], Variables.NumberOfTime60to89DaysPastDueNotWorse <= entered_sixtyninety[0],
                            Variables.NumberOfDependents <= entered_dependents[0])
    
    if not eligible_applicants:

        eligible_applicants.append([variable.id for variable in variable_instances])
        
    else:
        eligible_applicants.clear()
        eligible_applicants.append([variable.id for variable in variable_instances])

    if not statistics:

        calculate_statistics(entered_age, entered_income, entered_util, 
                        entered_thirtysixty, entered_debtratio, entered_minopenlines,
                        entered_ninety, entered_realestate, entered_sixtyninety,
                        entered_dependents)
    else:
        statistics.clear()
        calculate_statistics(entered_age, entered_income, entered_util, 
                        entered_thirtysixty, entered_debtratio, entered_minopenlines,
                        entered_ninety, entered_realestate, entered_sixtyninety,
                        entered_dependents)
    
    return jsonify({"items": eligible_applicants})

@array_api.route('/calculate_statistics', methods=['GET', 'POST'])
def calculate_statistics(entered_age, entered_income, entered_util,
                        entered_thirtysixty, entered_debtratio, entered_minopenlines,
                        entered_ninety, entered_realestate,
                        entered_sixtyninety, entered_dependents):

    number_of_apps = db.session.query(Variables).count()
    percent_accepted = (((max(map(len, eligible_applicants)))/(number_of_apps) * 100))
    statistics.append({"Percentage accepted: " : "%.2f" % percent_accepted})
    average_age = db.session.query(func.avg(Variables.age)) \
        .filter(Variables.age >= entered_age[0], Variables.age <= entered_age[1]) \
        .scalar()
    statistics.append({"Average age of accepted: " : "%.2f" % average_age})
    average_income = db.session.query(func.avg(Variables.MonthlyIncome)) \
        .filter(Variables.MonthlyIncome >= entered_income[0]) \
        .scalar()
    statistics.append({"Average monthly income of accepted: " : "%.2f" % average_income})
    average_util = db.session.query(func.avg(Variables.RevolvingUtilizationOfUnsecuredLines)) \
        .filter(Variables.RevolvingUtilizationOfUnsecuredLines <= entered_util[0]) \
        .scalar()
    statistics.append({"Average utilization of unsecured credit of accepted: " : "%.2f" % average_util})
    average_thirtysixty = db.session.query(func.avg(Variables.NumberOfTime30to59DaysPastDueNotWorse)) \
        .filter(Variables.NumberOfTime30to59DaysPastDueNotWorse <= entered_thirtysixty[0]) \
        .scalar()
    statistics.append({"Average number of 30 to 60 day delinquencies of accepted: " : "%.2f" % average_thirtysixty})
    average_debtratio = db.session.query(func.avg(Variables.DebtRatio)) \
        .filter(Variables.DebtRatio <= entered_debtratio[0]) \
        .scalar()
    statistics.append({"Average income to debt ratio of accepted: " : "%.2f" % average_debtratio})
    average_openlines = db.session.query(func.avg(Variables.NumberOfOpenCreditLinesAndLoans)) \
        .filter(Variables.NumberOfOpenCreditLinesAndLoans >= entered_minopenlines[0]) \
        .scalar()
    statistics.append({"Average number of open credit lines of accepted: " : "%.2f" % average_openlines})
    average_ninety = db.session.query(func.avg(Variables.NumberOfTimes90DaysLate)) \
        .filter(Variables.NumberOfTimes90DaysLate <= entered_ninety[0]) \
        .scalar()
    statistics.append({"Average number delinquencies over 90 days of accepted: " : "%.2f" % average_ninety})
    average_realestate = db.session.query(func.avg(Variables.NumberRealEstateLoansOrLines)) \
        .filter(Variables.NumberRealEstateLoansOrLines >= entered_realestate[0]) \
        .scalar()
    statistics.append({"Average number of real estate lines or loans of accepted: " : "%.2f" % average_realestate})
    average_sixtyninety = db.session.query(func.avg(Variables.NumberOfTime60to89DaysPastDueNotWorse )) \
        .filter(Variables.NumberOfTime60to89DaysPastDueNotWorse <= entered_sixtyninety[0]) \
        .scalar()
    statistics.append({"Average number of 60 to 90 day delinquencies of accepted: " : "%.2f" % average_sixtyninety})
    average_dependents = db.session.query(func.avg(Variables.NumberOfDependents)) \
        .filter(Variables.NumberOfDependents  <= entered_dependents[0]) \
        .scalar()
    statistics.append({"Average number dependents of accepted: " : "%.2f" % average_dependents})
   
    return jsonify({"stats": statistics})

@array_api.route('/accepted_applicants', methods=['GET', 'POST'])
def serve_all_accepted():

   return jsonify({"items": eligible_applicants})

@array_api.route('/applicants_stats', methods=['GET', 'POST'])
def serve_statistics():

    return jsonify({"stats": statistics })

