import pandas as pd
import sqlite3

def run_etl():
    # 1. EXTRACT
    print("--- Phase 1: Extracting ---")
    df = pd.read_csv('raw_sales.csv')

    # 2. TRANSFORM (Cleaning & Validation)
    print("--- Phase 2: Transforming ---")
    
    # Validation: Remove negative quantities
    df = df[df['quantity'] > 0]
    
    # Data Cleaning: Fill missing prices with the average price
    df['price'] = df['price'].fillna(df['price'].mean())
    
    # Formatting: Standardize the date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 3. LOAD
    print("--- Phase 3: Loading to SQL ---")
    conn = sqlite3.connect('sales_data.db')
    df.to_sql('cleaned_sales', conn, if_exists='replace', index=False)
    conn.close()
    
    print("ETL Job Finished Successfully!")

if __name__ == "__main__":
    run_etl()