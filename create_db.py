import pandas as pd
import sqlite3

print("Creating Database...")

# 1. Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('vr_analytics.db')

# 2. Load CSVs
df_telemetry = pd.read_csv('vr_telemetry.csv')
df_reports = pd.read_csv('vr_reports.csv')

# 3. Convert timestamps to string format for SQLite
df_telemetry['timestamp'] = pd.to_datetime(df_telemetry['timestamp']).astype(str)
df_reports['timestamp'] = pd.to_datetime(df_reports['timestamp']).astype(str)

# 4. Save to SQL
df_telemetry.to_sql('telemetry', conn, if_exists='replace', index=False)
df_reports.to_sql('reports', conn, if_exists='replace', index=False)

print("Database 'vr_analytics.db' created successfully.")
conn.close()