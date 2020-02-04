import pandas as pd
from sql_alchemy_db_instance import db
from app import create_app

app = create_app()
with app.app_context():
    engine = db.get_engine()
    csv_file_path = 'cs-test.csv'

    # Read CSV (cs-test.csv) with Pandas
    with open(csv_file_path, 'r') as file:
            df = pd.read_csv(file)

    # Insert to DB
    df.to_sql('APPLICANTS',
            con=engine,
            index_label='id',
            if_exists='replace',
            chunksize=100)

