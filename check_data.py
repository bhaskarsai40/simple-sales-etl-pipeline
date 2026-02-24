import sqlite3
import pandas as pd

# Connect to the database you created
conn = sqlite3.connect('sales_data.db')

# Write a SQL query to see the top 5 rows
query = "SELECT * FROM cleaned_sales LIMIT 5;"

# Read the SQL result into a Pandas table to print it nicely
df = pd.read_sql_query(query, conn)

print("--- Data inside your SQL Database ---")
print(df)

conn.close()