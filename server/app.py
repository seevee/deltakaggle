import os
from flask import Flask, render_template
from arrayAPI import array_api, Variables
from sql_alchemy_db_instance import db
import pandas as pd
import sqlalchemy.engine.url as url


project_dir = os.path.dirname(os.path.abspath(__file__))


def create_app():
    app = Flask(__name__,
        static_folder = "./dist/static",
        template_folder = "./dist"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "applicant-info.db"))
    print("printline at 20 with path name:    "    +   "sqlite:///{}".format(os.path.join(project_dir, "applicant-info.db")))
    print(vars(url.make_url("sqlite:///{}".format(os.path.join(project_dir, "applicant-info.db")))))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(array_api)

    return app

def setup_database(app):

    with app.app_context():
        print("line in 28 in app")
        db.create_all()
        print("line 30 in app")
            
            
        engine = db.get_engine()
        trainDF = pd.read_csv('cs-test.csv')

            
        trainDF.to_sql('APPLICANTS', con=engine, index_label='id', if_exists='replace')





