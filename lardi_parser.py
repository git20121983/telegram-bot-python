import requests
from bs4 import BeautifulSoup
from config import HEADERS

URL = "https://lardi-trans.com/log/search/gruz"

def fetch_cargo():
    r = requests.get(URL, headers=HEADERS, timeout=20)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "lxml")
    rows = soup.select("tr[data-id]")

    cargos = []

    for row in rows[:5]:
        cells = row.find_all("td")
        if len(cells) < 6:
            continue

        cargo = {
            "from": cells[2].get_text(strip=True),
            "to": cells[3].get_text(strip=True),
            "cargo": cells[4].get_text(strip=True),
            "price": cells[5].get_text(strip=True),
        }
        cargos.append(cargo)

    return cargos
