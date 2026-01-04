import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
LARDI_EMAIL = os.getenv("LARDI_EMAIL")
LARDI_PASSWORD = os.getenv("LARDI_PASSWORD")
MAX_RESULTS = int(os.getenv("MAX_RESULTS", 5))

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing")

