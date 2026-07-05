import requests

TOKEN = "8698232598:AAENfKnXvBo3tA3Z52IGf1r7Ylnv0cKhShc"
CHAT_ID = "8876505556"

def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)