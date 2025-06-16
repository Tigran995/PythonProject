
import os
import requests
from dotenv import load_dotenv
from typing import Dict, Union

load_dotenv()

API_KEY = os.getenv('ce4dbc52e33a630db652d86db610885f')
BASE_URL = "https://home.openweathermap.org/api_keys"


def convert_to_rub(transaction: Dict[str, Union[str, float]]) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction: Словарь с данными транзакции

    Returns:
        Сумма в рублях (float)
    """
    amount = transaction.get('amount', 0)
    currency = transaction.get('currency', 'RUB').upper()

    if currency == 'RUB':
        return float(amount)

    try:
        response = requests.get(
            BASE_URL,
            params={'base': currency, 'symbols': 'RUB'},
            headers={'apikey': API_KEY}
        )
        response.raise_for_status()
        rate = response.json()['rates']['RUB']
        return float(amount) * rate
    except (requests.RequestException, KeyError):
        return 0.0
