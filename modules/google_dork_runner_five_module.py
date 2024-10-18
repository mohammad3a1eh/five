from modules.core.pars import check_url
from modules.core.config import EXPORT_LOCATION, GOOGLE_API_KEY, GOOGLE_ENGINE_ID
from modules.core.value import get_datetime
from time import sleep


NAME = "Google Dork Runner"
DISCRIPTION = """
This module executes google dorks and receives the output of searches from googleapis
"""

REQUIREMENTS = []

import requests
import os


def run():
    website_url = input("Enter website_url: ")
    website_url = check_url(website_url)

    google_query = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={GOOGLE_ENGINE_ID}&q="

    with open("modules/assets/dorks.txt") as dorks_file:
        dorks = dorks_file.readlines()

    result = []

    for dork in dorks:
        query = dork.replace("{{{{}}}}", website_url).rstrip("\n")
        sleep(5)  # Just to avoid error "429 Client error: too many requests"

        try:
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/102.0.0.0 Safari/537.36"
            }

            response = requests.get(google_query+query, headers=headers)
            response.raise_for_status()

            response = response.json()
            if response["searchInformation"]["totalResults"] != "0":
                for item in response["items"]:
                    result.append(item["link"])

            print(f"Success fetching {query}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {query}: {e[:20]}")

    folder = website_url.replace('https://', '').replace('http://', '').replace('/', '_')
    filename = f'{get_datetime()}_google_dorks.txt'

    if not os.path.exists(os.path.join(EXPORT_LOCATION(), folder)):
        os.makedirs(os.path.join(EXPORT_LOCATION(), folder))

    with open(os.path.join(EXPORT_LOCATION(), folder, filename), 'w') as file:
        file.writelines(result)

    if len(result) != 0:
        print(f"{len(result)} result found!File saved as {folder}\\{filename}")
    else:
        print(f"0 result found!")
