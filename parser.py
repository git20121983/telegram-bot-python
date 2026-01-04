import re

def parse_query(text: str) -> dict:
    text = text.lower()

    cities = re.findall(r"[а-яёіїє]+", text)

    weight = re.search(r"(\d{1,2})\s*т", text)
    volume = re.search(r"(\d{1,3})\s*(куб|м3)", text)

    return {
        "from": cities[0] if len(cities) > 0 else None,
        "to": cities[1] if len(cities) > 1 else None,
        "weight": weight.group(1) if weight else None,
        "volume": volume.group(1) if volume else None,
        "date": "завтра" if "завтра" in text else "сегодня"
    }
