import pandas as pd
import requests
import json
import time

# --- CONFIGURATION ---
API_KEY = 'YOUR_API_KEY_HERE'  # <--- Replace this with your actual key
URL = 'https://api2.amplitude.com/2/httpapi'

print("Reading data...")
try:
    df = pd.read_csv('vr_telemetry.csv')
except FileNotFoundError:
    print("Error: Could not find 'vr_telemetry.csv'.")
    exit()

# Select just 10 events to test
events_to_send = df.head(10)

payload_events = []

print("Sending 10 'Live' events...")

for index, row in events_to_send.iterrows():
    event = {
        "user_id": str(row['user_id']),
        "event_type": row['event_type'],
        # CHANGE: We force the time to be NOW so it shows in Live View
        "time": int(time.time() * 1000), 
        "event_properties": {
            "voice_volume": row['voice_volume_db'],
            "asset_used": row['asset_used'],
            "x_coord": row['x_coord'],
            "y_coord": row['y_coord']
        }
    }
    payload_events.append(event)
    
    # Optional: Wait 0.5 seconds between events so they pop up one by one
    time.sleep(0.5) 

data = {
    "api_key": API_KEY,
    "events": payload_events
}

response = requests.post(URL, data=json.dumps(data))

if response.status_code == 200:
    print("✅ Sent! Look at your browser NOW.")
else:
    print(f"❌ Error: {response.text}")