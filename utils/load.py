import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import gspread
from google.oauth2.service_account import Credentials

def load_to_csv(df, file_path="products.csv"):
    try:
        df.to_csv(file_path, index=False)
        print(f"Data disimpan ke {file_path}")
    except Exception as e:
        print(f"Error CSV: {e}")

def load_to_google_sheets(df, spreadsheet_name, json_key_path):
    try:
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        creds = Credentials.from_service_account_file(json_key_path, scopes=scope)
        client = gspread.authorize(creds)
        sh = client.open(spreadsheet_name)
        worksheet = sh.get_worksheet(0)
        worksheet.clear()
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
        print("Data diunggah ke Google Sheets")
    except Exception as e:
        print(f"Error Google Sheets: {e}")

def load_to_postgresql(df, db_config):
    try:
        url = URL.create(
            drivername="postgresql+psycopg2",
            username=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port'],
            database=db_config['database'],
        )

        engine = create_engine(url)

        df.to_sql('competitor_products', engine, if_exists='replace', index=False)

        print("Data disimpan ke PostgreSQL")

    except Exception as e:
        print(f"Error PostgreSQL: {e}")
        return None