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

    # ✅ ТЕПЕРЬ ЭТО requests.Response
    print("STATUS:", response.status_code)
    print("URL:", response.url)
    print("HTML LENGTH:", len(response.text))

    soup = BeautifulSoup(response.text, "html.parser")

    cargos = []

    # Универсальный поиск по строкам таблицы
    for row in soup.select("tr"):
        text = row.get_text(" ", strip=True)

        if (
            from_city.lower() in text.lower()
            and to_city.lower() in text.lower()
        ):
            cargos.append({
                "title": text[:300],
                "phone": "См. на сайте Lardi"
            })

        if len(cargos) >= limit:
            break

    return cargos
