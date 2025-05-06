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
    Преобразует строку с датой в формате 'ГГГГ-ММ-ДД-Час-Минута-Секунда-Миллисекунда'
    в формат 'ДД_ММ_ГГГГ' (например, '2004-66-71' -> '02_04_2004').
    """
    try:
        date_parts = list(map(int, raw_date.split("-")))
        year = date_parts[0] % 10000  # Год из первых 4 циф
        month = date_parts[1] % 12     # Месяц (1-12)
        day = date_parts[2] % 31       # День (1-31)
        month = month if month != 0 else 12
        day = day if day != 0 else 31
        return f"{day:02}_{month:02}_{year}"
    except (IndexError, ValueError, TypeError):
        return "Некорректный формат даты"
