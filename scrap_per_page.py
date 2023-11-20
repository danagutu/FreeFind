import requests
from bs4 import BeautifulSoup
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("creds/oit-mentorship-programme-firebase-adminsdk-juuxr-8b6fa1a479.json")
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://oit-mentorship-programme-default-rtdb.europe-west1.firebasedatabase.app/'
    })

def download_event_details (url):
    response = requests.get(url)
    soup = response.text
    soup = BeautifulSoup(soup,"lxml")
    
    return soup

def extract_event_details (soup):
    event_title = soup.title.text.strip()
    event_date_time = soup.find("span", {"class":"eventDateTime"}).text.strip()
    event_location = soup.find("span", {"class": "eventVenue"}).text.strip()
    #event_description = soup.find("span", {"class": "contentBoxes"}).text.strip()
    #event_image = soup.find("span", {"class": "galleryIcon"}).text.strip()
    
    #### space for openai_test.py
    
    event_details = {
        "title": event_title,
        "date_time": event_date_time,
        "location": event_location,
        #"description": event_description,
        #"image": event_image,
        #"free_food": free_food,
        #"free_soft_drinks":free_soft_drinks,
        #"free_alc_drinks": free_alch_drinks,
    }

    return event_details

def get_id_from_url(url):
    url_parts = url.split("/")
    id = url_parts[-1]
    return id

def save_event_details_to_json (event_details):
    event_details_json = "event_details.json"
    with open(event_details_json, "w", encoding="utf-8") as json_file:
        json.dump(event_details, json_file, indent=2)

def save_event_details_to_firebase(event_details, id):
    print(event_details)
    print(id)
    try:
        # Reference to the database
        ref = db.reference('events')
        # Pushing the new event details
        ref.child(id).set(event_details)
    except Exception as e:
        print(e)

events = [
    "https://www.bristolsu.org.uk/groups/bems-bristol-engineering-mathematics-society/events/board-games-and-pizza-13d3",
    "https://www.bristolsu.org.uk/groups/japanese-society-434d/events/japanese-culture-fest-with-global-lounge",
    "https://www.bristolsu.org.uk/groups/kharis-on-campus-9e28/events/kharis-on-campus-fellowship-5983",
    "https://www.bristolsu.org.uk/groups/acs-african-caribbean-society-b18b/events/caribbean-meet-up",
    "https://www.bristolsu.org.uk/events/international-students-quiz-night-d48a",
    "https://www.bristolsu.org.uk/groups/the-cell-a1b8/events/movie-night-1b8b",
    "https://www.bristolsu.org.uk/events/global-food-fair-0481",
    "https://www.bristolsu.org.uk/events/womens-network-tote-bag-and-tapestry-painting",
    "https://www.bristolsu.org.uk/events/climate-conversations-and-crafts",
    "https://www.bristolsu.org.uk/groups/mechsoc-mechanical-engineering-society-c13d/events/mechsoc-alumni-networking-event"
]

if __name__ == "__main__":
    for url in events:
        id = get_id_from_url(url)
        soup = download_event_details(url)
        event_details = extract_event_details(soup)
        save_event_details_to_firebase(event_details, id)