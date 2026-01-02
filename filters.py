def filter_cargos(cargos: list):
    """
    Фильтрация грузов под TransEuroLogistics
    """
    filtered = []

    for c in cargos:
        # Простейшая защита от пустых записей
        if not c.get("route"):
            continue

        # Можно расширять под бизнес-логику
        filtered.append(c)

    return filtered