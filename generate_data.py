import pandas as pd
import numpy as np
import uuid
import datetime
import random

# Configuration
NUM_USERS = 200
START_TIME = datetime.datetime.now() - datetime.timedelta(days=7)

print("Initializing Simulation...")

# 1. Create Users
users = []
for _ in range(NUM_USERS):
    # 10% of users are "Griefers" (Bad Actors)
    u_type = np.random.choice(['Normal', 'Griefer'], p=[0.90, 0.10])
    users.append({'user_id': str(uuid.uuid4()), 'user_type': u_type})

# 2. Generate Telemetry (Movement, Voice, Actions)
telemetry_data = []
report_data = []

print(f"Simulating {NUM_USERS} users...")

for user in users:
    # Griefers are more active and chaotic
    session_events = random.randint(20, 100) if user['user_type'] == 'Griefer' else random.randint(10, 40)
    current_time = START_TIME + datetime.timedelta(minutes=random.randint(0, 1000))
    session_id = str(uuid.uuid4())
    
    for _ in range(session_events):
        current_time += datetime.timedelta(seconds=random.randint(5, 30))
        
        # Behavior Logic
        if user['user_type'] == 'Griefer':
            voice_vol = np.random.normal(85, 10) # Loud
            interaction = np.random.choice(['spawn_object', 'touch', 'idle'], p=[0.6, 0.3, 0.1])
            asset = np.random.choice(['asset_gun_01', 'asset_siren', 'cube'], p=[0.45, 0.45, 0.1])
        else:
            voice_vol = np.random.normal(40, 5) # Quiet
            interaction = np.random.choice(['spawn_object', 'wave', 'explore'], p=[0.1, 0.3, 0.6])
            asset = np.random.choice(['cube', 'paintbrush', 'flower'], p=[0.3, 0.3, 0.4])

        # Log the event
        event = {
            'event_id': str(uuid.uuid4()),
            'user_id': user['user_id'],
            'session_id': session_id,
            'timestamp': current_time,
            'event_type': interaction,
            'voice_volume_db': round(voice_vol, 1),
            'asset_used': asset,
            'x_coord': round(random.uniform(0, 100), 2),
            'y_coord': round(random.uniform(0, 100), 2)
        }
        telemetry_data.append(event)

        # 3. Generate Reports (The "Safety" Aspect)
        if user['user_type'] == 'Griefer' and (voice_vol > 80 or asset in ['asset_gun_01', 'asset_siren']):
            if random.random() > 0.8: # 20% chance of being reported
                report_data.append({
                    'report_id': str(uuid.uuid4()),
                    'reported_user_id': user['user_id'],
                    'session_id': session_id,
                    'reason': 'Harassment/Griefing',
                    'timestamp': current_time + datetime.timedelta(seconds=random.randint(10, 60))
                })

# Save to CSV
df_tel = pd.DataFrame(telemetry_data)
df_rep = pd.DataFrame(report_data)

df_tel.to_csv('vr_telemetry.csv', index=False)
df_rep.to_csv('vr_reports.csv', index=False)

print(f"Success! Generated {len(df_tel)} telemetry events and {len(df_rep)} reports.")