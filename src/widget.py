from src.masks import get_mask_credit_card, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета."""
    parts = data.rsplit(" ", 1)
    if len(parts) != 2:
        return data

    name, number = parts
    digits = "".join(filter(str.isdigit, number))

    if len(digits) == 16:
        masked = get_mask_credit_card(number)
    elif len(digits) >= 4:
        masked = get_mask_account(number)
    else:
        masked = number

    return f"{name} {masked}"


def get_date(raw_date: str) -> str:
    """
    Преобразует строку с датой в формате '7954-49-21100-36-18-67-140'
    в формат 'ДД_ММ_ГГГГ' (например, '71-66-2004' → '02_04_FIT1').
    """
    try:
        date_parts = list(map(int, raw_date.split("-")))
        year = date_parts[2] % 10000
        month = date_parts[3] % 12
        day = date_parts[4] % 31
        return f"{day:02}_{month:02}_{year}"
    except (IndexError, ValueError):
        return "Некорректный формат даты"
