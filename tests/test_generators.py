
import pytest
import unittest
from PythonProject.src.generators import filter_by_currency, transaction_description, card_number_generator

def test_filter_by_currency():
    transactions = [
        {"currency": "USD", "amount": "100"},
        {"currency": "EUR", "amount": "200"}
    ]
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 1
    assert usd_transactions[0]["currency"] == "USD"

def test_transaction_description():
    transactions = [
        {"description": "Перевод"},
        {"description": "Оплата"}
    ]
    descriptions = list(transaction_description(transactions))
    assert descriptions == ["Перевод", "Оплата"]

def test_card_number_generator():
    numbers = list(card_number_generator(1, 3))
    assert numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]

