# lardi.py
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "uk-UA,ru;q=0.9",
    "Referer": "https://lardi-trans.com/"
}

def search_lardi(from_city="", to_city="", limit=5, cookies=None):
    url = "https://lardi-trans.com/ru/gruz/"

    session = requests.Session()
    session.headers.update(HEADERS)

    if cookies:
        session.cookies.update(cookies)

    response = session.get(url, timeout=20)
    soup = BeautifulSoup(response.text, "html.parser")

    cargos = []

    rows = soup.find_all("tr")

    for row in rows:
        text = row.get_text(" ", strip=True)

        # 🔑 главное условие — строка не пустая и не короткая
        if len(text) < 40:
            continue

        cargos.append({
            "title": text[:500]
        })

        if len(cargos) >= limit:
            break

    return cargos
