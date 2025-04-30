def get_mask_credit_card(card_number: str) -> str:
    """Маскирует номер карты в формате 'XXXX XX** **** XXXX'."""
    digits = "".join(filter(str.isdigit, card_number))
    if len(digits) != 16:
        return card_number
    return f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"


def get_mask_account(account: str) -> str:
    """Маскирует номер счета в формате '**XXXX'."""
    digits = "".join(filter(str.isdigit, account))
    if len(digits) < 4:
        return account
    return f"**{digits[-4:]}"