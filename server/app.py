import os
from flask import Flask
from arrayAPI import array_api
from sql_alchemy_db_instance import db
import pandas as pd

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app():
    app = Flask(__name__,
        static_folder = './dist/static',
        template_folder = './dist')
    if os.environ['RUN_ENVIRONMENT'] == 'network':
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=os.environ['DB_USER'],pw=os.environ['DB_PASS'],url=os.environ['DB_URL'],db=os.environ['DB_NAME'])
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(os.path.join(project_dir, '../db', 'deltakaggle.db'))
    app.config['SQLALCHEMY_ECHO'] = True
    db.init_app(app)
    app.register_blueprint(array_api)

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()
        return

