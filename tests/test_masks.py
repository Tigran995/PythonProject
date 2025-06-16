import pytest
from masks import get_mask_card_number, get_mask_account

# Фикстуры для тестов карт и счетов

@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234567812345678", "1234 5678 **** 5678"),
        ("1234", "Неверный номер карты"),  # Некорректная длина
        ("", "Неверный номер карты")        # Пустая строка
    ]


@pytest.fixture
def account_numbers():
    return [
        ("12345678901234567890", "**7890"),
        ("98765432109876543210", "**3210"),
        ("123", "Неверный номер счета"),    # Некорректная длина
        ("", "Неверный номер счета")        # Пустая строка
    ]

# Параметризованные тесты для карт
def test_get_mask_card_number(card_numbers):
    for number, expected in card_numbers:
        assert get_mask_card_number(number) == expected


# Параметризованные тесты для счетов
def test_get_mask_account(account_numbers):
    for number, expected in account_numbers:
        assert get_mask_account(number) == expected
