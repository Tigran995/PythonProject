import pytest
from PythonProject.src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "operationAmount": {
                "amount": "9824.07",
                "currency": {"code": "USD"}
            },
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {
                "amount": "79114.93",
                "currency": {"code": "USD"}
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {
                "amount": "43318.34",
                "currency": {"code": "RUB"}
            },
            "description": "Перевод со счета на счет",
        },
    ]


def test_filter_by_currency(sample_transactions):
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_transactions)


def test_filter_by_currency_empty(sample_transactions):
    eur_transactions = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(eur_transactions) == 0


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
    ]


@pytest.mark.parametrize("start, end, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000", "0000 0000 0001 0001"]),
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected
