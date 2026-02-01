import os
import time
import requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def wyslij_wiadomosc(tekst):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": tekst
    }
    r = requests.post(url, json=payload)
    print(r.text)

if __name__ == "__main__":
    while True:
        wyslij_wiadomosc("✅ TEST OK – bot działa (heartbeat)")
        time.sleep(30)
