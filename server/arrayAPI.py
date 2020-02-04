from flask import Blueprint, jsonify, request
from models import Variables
from sql_alchemy_db_instance import db
from sqlalchemy.sql import func

"""
app does not clear accepted applicants at refresh of browser
"""

array_api = Blueprint('array_api', __name__)

@array_api.route('/user_vars', methods=['GET', 'POST'])
def serve_user_vars():

    age_min = request.json['age_item'][0]
    age_max = request.json['age_item'][1]
    income = request.json['income_item'][0]
    util = request.json['util_item'][0]
    thirtysixty = request.json['thirtysixty_item'][0]
    debtratio = request.json['debtratio_item'][0]
    minopenlines = request.json['minlines_item'][0]
    ninety = request.json['ninety_item'][0]
    realestate = request.json['realestate_item'][0]
    sixtyninety = request.json['sixtyninety_item'][0]
    dependents = request.json['dependents_item'][0]

    variable_instances = db.session.query(Variables).filter(Variables.Age >= age_min, Variables.Age <= age_max,
                            Variables.MonthlyIncome >= income, Variables.RevolvingUtilizationOfUnsecuredLines <= util,
                            Variables.NumberOfTime30to59DaysPastDueNotWorse <= thirtysixty, Variables.DebtRatio <= debtratio,
                            Variables.NumberOfOpenCreditLinesAndLoans >= minopenlines, Variables.NumberOfTimes90DaysLate <= ninety,
                            Variables.NumberRealEstateLoansOrLines >= realestate, Variables.NumberOfTime60to89DaysPastDueNotWorse <= sixtyninety,
                            Variables.NumberOfDependents <= dependents)

    calculate_statistics(age_min, age_max, income, util,
            thirtysixty, debtratio, minopenlines,
            ninety, realestate, sixtyninety,
            dependents)

    return jsonify({'items': [variable.id for variable in variable_instances]})

@array_api.route('/calculate_statistics', methods=['GET', 'POST'])
def calculate_statistics(age_min, age_max, income, util,
                        thirtysixty, debtratio, minopenlines,
                        ninety, realestate,
                        sixtyninety, dependents):

    statistics = []
    number_of_apps = db.session.query(Variables).count()
    percent_accepted = (((max(map(len, eligible_applicants)))/(number_of_apps) * 100))
    statistics.append({'Percentage accepted: ' : '%.2f' % percent_accepted})
    average_age = db.session.query(func.avg(Variables.Age)) \
        .filter(Variables.Age >= age_min, Variables.Age <= age_max) \
        .scalar()
    statistics.append({'Average age of accepted: ' : '%.2f' % average_age})
    average_income = db.session.query(func.avg(Variables.MonthlyIncome)) \
        .filter(Variables.MonthlyIncome >= income) \
        .scalar()
    statistics.append({'Average monthly income of accepted: ' : '%.2f' % average_income})
    average_util = db.session.query(func.avg(Variables.RevolvingUtilizationOfUnsecuredLines)) \
        .filter(Variables.RevolvingUtilizationOfUnsecuredLines <= util) \
        .scalar()
    statistics.append({'Average utilization of unsecured credit of accepted: ' : '%.2f' % average_util})
    average_thirtysixty = db.session.query(func.avg(Variables.NumberOfTime30to59DaysPastDueNotWorse)) \
        .filter(Variables.NumberOfTime30to59DaysPastDueNotWorse <= thirtysixty) \
        .scalar()
    statistics.append({'Average number of 30 to 60 day delinquencies of accepted: ' : '%.2f' % average_thirtysixty})
    average_debtratio = db.session.query(func.avg(Variables.DebtRatio)) \
        .filter(Variables.DebtRatio <= debtratio) \
        .scalar()
    statistics.append({'Average income to debt ratio of accepted: ' : '%.2f' % average_debtratio})
    average_openlines = db.session.query(func.avg(Variables.NumberOfOpenCreditLinesAndLoans)) \
        .filter(Variables.NumberOfOpenCreditLinesAndLoans >= minopenlines) \
        .scalar()
    statistics.append({'Average number of open credit lines of accepted: ' : '%.2f' % average_openlines})
    average_ninety = db.session.query(func.avg(Variables.NumberOfTimes90DaysLate)) \
        .filter(Variables.NumberOfTimes90DaysLate <= ninety) \
        .scalar()
    statistics.append({'Average number delinquencies over 90 days of accepted: ' : '%.2f' % average_ninety})
    average_realestate = db.session.query(func.avg(Variables.NumberRealEstateLoansOrLines)) \
        .filter(Variables.NumberRealEstateLoansOrLines >= realestate) \
        .scalar()
    statistics.append({'Average number of real estate lines or loans of accepted: ' : '%.2f' % average_realestate})
    average_sixtyninety = db.session.query(func.avg(Variables.NumberOfTime60to89DaysPastDueNotWorse )) \
        .filter(Variables.NumberOfTime60to89DaysPastDueNotWorse <= sixtyninety) \
        .scalar()
    statistics.append({'Average number of 60 to 90 day delinquencies of accepted: ' : '%.2f' % average_sixtyninety})
    average_dependents = db.session.query(func.avg(Variables.NumberOfDependents)) \
        .filter(Variables.NumberOfDependents <= dependents) \
        .scalar()
    statistics.append({'Average number dependents of accepted: ' : '%.2f' % average_dependents})
   
    return jsonify({'stats': statistics})

@array_api.route('/accepted_applicants', methods=['GET', 'POST'])
def serve_all_accepted():

   return jsonify({'items': eligible_applicants})

@array_api.route('/applicants_stats', methods=['GET', 'POST'])
def serve_statistics():

    return jsonify({'stats': statistics })

