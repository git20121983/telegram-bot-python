# lardi.py
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "uk-UA,ru;q=0.9",
    "Referer": "https://lardi-trans.com/"
}

def search_lardi(from_city, to_city, limit=5, cookies=None):
    url = "https://lardi-trans.com/ru/gruz/"

    session = requests.Session()
    session.headers.update(HEADERS)

    if cookies:
        session.cookies.update(cookies)

    response = session.get(url, timeout=20)

    soup = BeautifulSoup(response.text, "html.parser")

    cargos = []

    # 🔑 В Lardi грузы — это строки таблицы с данными
    rows = soup.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue

        text = row.get_text(" ", strip=True)

        cargos.append({
            "title": text[:400],
            "phone": "Откройте груз на Lardi"
        })

        if len(cargos) >= limit:
            break

    return cargos
