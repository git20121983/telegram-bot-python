import requests
from bs4 import BeautifulSoup

BASE_URL = "https://lardi-trans.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/121.0 Safari/537.36"
    ),
    "Accept-Language": "uk-UA,ru;q=0.9",
}

class LardiClient:
    def __init__(self, email: str, password: str):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
        self.login(email, password)

    def login(self, email: str, password: str):
        self.session.get(f"{BASE_URL}/login")

        payload = {
            "email": email,
            "password": password
        }

        r = self.session.post(f"{BASE_URL}/login", data=payload)

        if r.status_code != 200:
            raise RuntimeError("Lardi login failed")

    def search(self, from_city: str, to_city: str):
        r = self.session.get(
            f"{BASE_URL}/gruz",
            params={"from": from_city, "to": to_city},
            timeout=20
        )

        if r.status_code != 200:
            return []

        soup = BeautifulSoup(r.text, "lxml")
        cargos = []

        for item in soup.select("div.gruz-item"):
            try:
                cargos.append({
                    "from": item.select_one(".route-from").text.strip(),
                    "to": item.select_one(".route-to").text.strip(),
                    "weight": item.select_one(".weight").text.strip(),
                    "price": item.select_one(".price").text.strip(),
                    "phone": item.select_one(".phone").text.strip(),
                })
            except:
                continue

        return cargos
