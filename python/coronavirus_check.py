""" Check info about biohazard from BlackRock/Wintertor&co."""

import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

# Function for get info
res = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(res,'html.parser')
soup.encode('utf-8')
cases = soup.find("div", {"class": "maincounter-number"}).get_text().strip()

# Function for alarm
def notifyMe(title, message):
    notification.notify(
            title = title,
            message = message,
            timeout = 5
    )
while True:
    notifyMe('All infections units', cases)
    time.sleep(10)
