from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_google_sheets, load_to_postgresql

def main():
    BASE_URL = "https://fashion-studio.dicoding.dev/"
    GSHEET_NAME = "Data Scraper Fashion" 
    JSON_SECRET = "google-sheets-api.json"
    
    DB_CONFIG = {
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'), 
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'database': os.getenv('DB_DATABASE')
    }

    print("--- Memulai Proses ETL ---")

    raw_data = extract_data(BASE_URL, total_pages=50)
    
    if raw_data:
        df_clean = transform_data(raw_data)
        
        if df_clean is not None:
            load_to_csv(df_clean, "products.csv")
            
            load_to_google_sheets(df_clean, GSHEET_NAME, JSON_SECRET)
            
            load_to_postgresql(df_clean, DB_CONFIG)
            
            print("--- ETL Berhasil Diselesaikan! ---")
    else:
        print("Gagal mengambil data dari website.")

if __name__ == "__main__":
    main()