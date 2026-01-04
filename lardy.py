import requests
from bs4 import BeautifulSoup
from config import LARDI_EMAIL, LARDI_PASSWORD, MAX_RESULTS

session = requests.Session()
BASE_URL = "https://lardi-trans.com"


def login():
    session.get(f"{BASE_URL}/login")

    payload = {
        "email": LARDI_EMAIL,
        "password": LARDI_PASSWORD
    }

    r = session.post(f"{BASE_URL}/login", data=payload)
    if r.status_code != 200:
        raise RuntimeError("Lardi login failed")


def search_lardi(text: str):
    if not session.cookies:
        login()

    params = {
        "search": text
    }

    r = session.get(f"{BASE_URL}/gruz/search", params=params)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
    rows = soup.select(".cargo-row")[:MAX_RESULTS]

    result = []

    for row in rows:
        result.append({
            "from": row.select_one(".from").text.strip(),
            "to": row.select_one(".to").text.strip(),
            "weight": row.select_one(".weight").text.strip(),
            "volume": row.select_one(".volume").text.strip(),
            "date": row.select_one(".date").text.strip(),
            "phone": row.select_one(".phone").text.strip(),
        })

    return result
