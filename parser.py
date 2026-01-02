import re

def parse_query(text: str):
    text = text.lower()
    cities = re.findall(r"[а-яёіїє]+", text)

    return {
        "from": cities[0] if len(cities) > 0 else None,
        "to": cities[1] if len(cities) > 1 else None
    }