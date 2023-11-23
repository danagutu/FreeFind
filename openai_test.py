import openai
import os
import json
import scrap_per_page
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

test_mode = False

# retrieves the OpenAI API Key
file_path = "creds/openai_creds.json"
with open(file_path, "r") as file:
    openai_creds = json.loads(file.read())
key = openai_creds["key"]

openai.api_key  = key
events_ref = db.reference('/events')

def save_free_stuff(free_stuff, id):
    try:
        # Pushing the new event details
        events_ref.child(id).child("free_stuff").set(free_stuff)
    except Exception as e:
        print(e)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    free_stuff = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # degree of randomness of the model's output
    )
    return free_stuff.choices[0].message["content"]


pre_prompt = f"""
You will be given the description of an event that has free entry. This event is for students. 
Your task is to perform the follwoing actions:
1. Read event_description and extract the sentences that contain any food or drink items.
2. Identify if the sentences you extracted contain any of the following: any food items, soft drinks, alcoholic drinks.
3. Output a dictionary called "event_details" with the following keys: "free_food", "free_soft_drinks", "free_alch_drinks".
The values should be boolean.
If any of the sentences mention any food items, then assign the value True to free_food. Else, assign False.
If any of the sentences mention non-alcoholic drinks, then assign the value True to free_soft_drinks. Else, assign False.
If any of the sentences mention alcoholic drinks, then assign the value True to free_alcoholic_drinks. Else, assign False.
"""


def get_id_from_url(url):
    url_parts = url.split("/")
    id = url_parts[-1]
    return id

#def save_event_details_to_json (event_details):
 #   event_details_json = "event_details.json"
  #  with open(event_details_json, "w", encoding="utf-8") as json_file:
   #     json.dump(event_details, json_file, indent=2)



if __name__ == "__main__":
    if test_mode:
        print(test_mode)

    else:
        events = events_ref.get()

        for event_id in events:
            print(event_id)

            description = events[event_id]["description"]
            print(description)

            prompt = pre_prompt + description
            free_stuff = get_completion(prompt)
            print(free_stuff)

            save_free_stuff(free_stuff, event_id)
            print("SAVED!")