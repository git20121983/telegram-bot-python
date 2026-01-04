import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
LARDI_COOKIES = os.getenv("LARDI_COOKIES")
LARDI_USER_AGENT = os.getenv("LARDI_USER_AGENT")

HEADERS = {
    "User-Agent": LARDI_USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": LARDI_COOKIES,
}

# Telegram
BOT_TOKEN = "8133529792:AAGfz8tC8JhGQe7kMBVi1j_DeBZpeo4wlGk"

# Lardi (ОБЯЗАТЕЛЬНО отдельный аккаунт)
LARDI_EMAIL = "Reno3"
LARDI_PASSWORD = "Katrusya_200680"

# Поведение
MAX_RESULTS = 5
REQUEST_TIMEOUT = 20
