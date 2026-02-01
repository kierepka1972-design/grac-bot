import os
import requests
import time

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_message("✅ TEST OK — bot działa poprawnie.\nPowiadomienia GRAĆ / NIE GRAĆ będą wysyłane automatycznie.")
    while True:
        time.sleep(60)
