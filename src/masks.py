from typing import Optional
from .logging_config import setup_logger

# Инициализация логера
logger = setup_logger('masks', 'masks.log')


def mask_card_number(card_number: str) -> Optional[str]:
    """
    Маскирует номер карты, оставляя видимыми первые 6 и последние 4 цифры.

    Args:
        card_number: Номер карты в виде строки

    Returns:
        Замаскированный номер карты или None, если номер некорректен
    """
    if not card_number or len(card_number) < 16 or not card_number.isdigit():
        logger.error(f'Некорректный номер карты: {card_number}')
        return None

    masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f'Успешно замаскирован номер карты: {masked}')
    return masked


def mask_account_number(account_number: str) -> Optional[str]:
    """
    Маскирует номер счета, оставляя видимыми последние 4 цифры.

    Args:
        account_number: Номер счета в виде строки

    Returns:
        Замаскированный номер счета или None, если номер некорректен
    """
    if not account_number or len(account_number) < 4 or not account_number.isdigit():
        logger.error(f'Некорректный номер счета: {account_number}')
        return None

    masked = f"**{account_number[-4:]}"
    logger.info(f'Успешно замаскирован номер счета: {masked}')
    return masked
