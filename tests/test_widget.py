from src.widget import mark_account_card, get_date


def test_mark_account_card():
    assert mark_account_card("Visa Platform 786979228966051") == "Visa Platform 7869 79** **** 6051"
    assert mark_account_card("Счет 79554108030135874396") == "Счет **4396"
    assert mark_account_card("InvalidInput123") == "InvalidInput123"


def test_get_date():
    assert get_date("7954-49-21100-36-18-67-140") == "18_36_21100"
    assert get_date("invalid-date") == "Некорректный формат даты"
