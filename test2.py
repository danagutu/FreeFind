import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("creds/oit-mentorship-programme-firebase-adminsdk-juuxr-8b6fa1a479.json")
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://oit-mentorship-programme-default-rtdb.europe-west1.firebasedatabase.app/'
    })



events_ref = db.reference('/events')

# Retrieve data for all events
events_data = events_ref.get()

# Access and print each JSON object
for event_id, event_data in events_data.items():
    print(f"Event ID: {event_id}")
    print("Event Data:")
    print(event_data)
