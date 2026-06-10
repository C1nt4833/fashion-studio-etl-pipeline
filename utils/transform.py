import pandas as pd
import numpy as np

def transform_data(raw_data):
    """
    Melakukan pembersihan dan transformasi data (Kriteria 1 & Skilled).
    """
    try:
        if not raw_data:
            return None
            
        df = pd.DataFrame(raw_data)
        
        df = df[df['Title'] != "Unknown Product"]
        
        df['Price'] = df['Price'].replace('Price Unavailable', np.nan)
        
        df = df[~df['Rating'].str.contains("Invalid Rating|Not Rated", na=False)]
        
        df['Price'] = df['Price'].str.replace(r'[\$,]', '', regex=True)
        df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
        df['Price'] = df['Price'] * 16000
        
        df['Rating'] = df['Rating'].str.extract(r'(\d+\.\d+|\d+)').astype(float)
        
        df['Colors'] = df['Colors'].str.extract(r'(\d+)').astype(int)
        
        df['Size'] = df['Size'].str.replace('Size: ', '', case=False).str.strip()
        df['Gender'] = df['Gender'].str.replace('Gender: ', '', case=False).str.strip()
        
        df = df.drop_duplicates()
        df = df.dropna()
        
        print(f"Transformasi selesai. Data bersih: {len(df)} baris.")
        return df

    except Exception as e:
        print(f"Error pada tahap Transform: {e}")
        return None