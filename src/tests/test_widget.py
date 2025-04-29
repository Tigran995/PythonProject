from src.widget import mark_account_card

def test_mark_account_card():
    # Карта
    assert mark_account_card("Visa 7080792289060531") == "Visa 7080 79** **** 0531"
    # Счет
    assert mark_account_card("Счет 7355418613013574195") == "Счет **74195"
    # Некорректный ввод
    assert mark_account_card("InvalidInput123") == "InvalidInput123"
