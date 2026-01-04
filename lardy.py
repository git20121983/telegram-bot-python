# lardi.py
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ru-UA,ru;q=0.9",
    "Referer": "https://lardi-trans.com/"
}

def search_lardi(from_city, to_city, limit=5, cookies=None):
    url = "https://lardi-trans.com/ru/gruz/"

    params = {
        "from": from_city,
        "to": to_city
    }

    session = requests.Session()
    session.headers.update(HEADERS)
    session.cookies.update(cookies)

    response = session.get(url, params=params, timeout=15)

    if response.status_code != 200:
        raise Exception(f"Lardi error: {response.status_code}")

    soup = BeautifulSoup(response.text, "html.parser")
    cargos = []

    for card in soup.select(".cargo-item")[:limit]:
        title = card.select_one(".cargo-title")
        phone = card.select_one(".phone")

        cargos.append({
            "title": title.text.strip() if title else "Без описания",
            "phone": phone.text.strip() if phone else "Контакт скрыт"
        })

    return cargos
