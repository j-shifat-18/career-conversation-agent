import requests
from config import PUSHOVER_USER_KEY, PUSHOVER_API_TOKEN

def send_notification(title, message):
    url = "https://api.pushover.net/1/messages.json"

    data = {
        "token": PUSHOVER_API_TOKEN,
        "user": PUSHOVER_USER_KEY,
        "title": title,
        "message": message
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("Pushover Error:", response.text)







    