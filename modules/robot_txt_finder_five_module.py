from modules.core.pars import check_url
from modules.core.config import EXPORT_LOCATION
from modules.core.value import get_datetime

NAME = "'Robot.txt' Finder"
DISCRIPTION = """
This module downloads and saves the robot.txt file if possible
"""

REQUIREMENTS = []

import requests
import os


def run():
    website_url = input("Enter website_url: ")
    website_url = check_url(website_url)

    robots_url = website_url + '/robots.txt'

    try:
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/102.0.0.0 Safari/537.36"
        }
        response = requests.get(robots_url, headers=headers)
        response.raise_for_status()

        folder = website_url.replace('https://', '').replace('http://', '').replace('/', '_')
        filename = f'{get_datetime()}_robots.txt'

        if not os.path.exists(os.path.join(EXPORT_LOCATION(), folder)):
            os.makedirs(os.path.join(EXPORT_LOCATION(), folder))

        with open(os.path.join(EXPORT_LOCATION(), folder, filename), 'w') as file:
            file.write(response.text)

        print(f"File saved as {folder}\\{filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching robots.txt: {e}")

