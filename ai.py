import re

def parse_query(text: str) -> dict:
    data = {
        "from_city": "",
        "to_city": "",
        "weight": "",
        "volume": "",
        "date": ""
    }

    route = re.search(r"(\w+)\s*(?:-|→)\s*(\w+)", text)
    if route:
        data["from_city"] = route.group(1)
        data["to_city"] = route.group(2)

    weight = re.search(r"(\d+)\s*(т|тонн)", text, re.IGNORECASE)
    if weight:
        data["weight"] = weight.group(1)

    volume = re.search(r"(\d+)\s*(м3|м³|куб)", text, re.IGNORECASE)
    if volume:
        data["volume"] = volume.group(1)

    if "сегодня" in text.lower():
        data["date"] = "сегодня"
    elif "завтра" in text.lower():
        data["date"] = "завтра"

    return data