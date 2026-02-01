def wyslij_wiadomosc(tekst):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": str(CHAT_ID),
        "text": tekst
    }
    r = requests.post(url, json=payload)
    print(r.text)
