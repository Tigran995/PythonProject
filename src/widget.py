def mark_account_card(data: str) -> str:
    """
    Маскирует номер карты или счета в строке формата "Тип Номер".
    Возвращает строку с замаскированным номером.
    """
    parts = data.rsplit(" ", 1)
    if len(parts) != 2:
        return data

    name, number = parts
    digits = "".join(filter(str.isdigit, number))

    if len(digits) == 16:  # Карта
        masked = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    elif len(digits) >= 4:  # Счет
        masked = f"**{digits[-4:]}"
    else:
        masked = number  # Некорректный номер

    return f"{name} {masked}"
