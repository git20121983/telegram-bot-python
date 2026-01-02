import requests

BASE_URL = "https://lardi-trans.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "uk-UA,ru;q=0.9",
    "Referer": BASE_URL
}

def login_lardi(email: str, password: str) -> requests.Session:
    session = requests.Session()
    session.headers.update(HEADERS)

    # 1️⃣ открываем страницу логина (получаем csrf/cookies)
    session.get(f"{BASE_URL}/login")

    # 2️⃣ отправляем форму логина
    payload = {
        "email": email,
        "password": password
    }

    r = session.post(f"{BASE_URL}/login", data=payload)

    if r.status_code != 200:
        raise Exception("❌ Ошибка логина в Lardi")

    return session