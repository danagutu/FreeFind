import requests
from bs4 import BeautifulSoup
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from scrap_per_page import *

# cred = credentials.Certificate("creds/oit-mentorship-programme-firebase-adminsdk-juuxr-8b6fa1a479.json")
# firebase_admin.initialize_app(cred, {
#         'databaseURL': 'https://oit-mentorship-programme-default-rtdb.europe-west1.firebasedatabase.app/'
#     })

url = "https://www.bristolsu.org.uk/events"

def download_event_page (url):
    response = requests.get(url)
    soup = response.text
    soup = BeautifulSoup(soup,"lxml")
    
    return soup

def get_event_urls (soup):
    container = soup.find("div", {"class": "uc-event-page-wrapper"})
    li_tags = container.find_all('li', recursive=True)

    list_urls = []

    for list_element in li_tags:
        container_link = list_element.find("a", {"class": "event-box"})["href"]
        event_url = "https://www.bristolsu.org.uk" + container_link
        list_urls.append(event_url)
    
    return list_urls

if __name__ == "__main__":
    event_list_page_soup = download_event_page(url)
    list_urls = get_event_urls(event_list_page_soup)

    for url in list_urls:
        id = get_id_from_url(url)
        soup = download_event_details(url)
        event_details = extract_event_details(soup, url)
        save_event_details_to_firebase(event_details, id)
    
