import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("creds/oit-mentorship-programme-firebase-adminsdk-juuxr-8b6fa1a479.json")
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://oit-mentorship-programme-default-rtdb.europe-west1.firebasedatabase.app/'
    })


def get_event_description_from_firebase():


    # Reference to the database
    ref = db.reference('events/description')
    # Pushing the new event details
    prompt_description = ref.get()
    return prompt_description


def get_test_prompt():
    with open("test_content/description.txt", "r", encoding="utf-8") as file:
        prompt_description = get_event_description_from_firebase()
        #prompt_description = file.read()
    
    test_prompt = prompt_description
    return test_prompt

print(get_test_prompt())