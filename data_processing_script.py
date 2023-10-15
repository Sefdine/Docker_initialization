import sqlite3
import pandas as pd

# Simulated data ingestion
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [35, 28, 29, 42]
}
df = pd.DataFrame(data)

# Data processing
processed_data = df.groupby('Name').mean()

# Storing data in SQLite database
conn = sqlite3.connect('database.db')
processed_data.to_sql('processed_data', conn, if_exists='replace', index=False)
conn.close()

print("Data processing and storage complete.")
