import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ce4dbc52e33a630db652d86db610885f')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'


def convert_to_rub(transaction: Dict[str, Any]) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли.

    """
    if not transaction or 'amount' not in transaction or 'currency' not in transaction:
        return None

    amount = transaction['amount']
    currency = transaction['currency']

    if currency == 'RUB':
        return float(amount)

    if currency in ('USD', 'EUR'):
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
            return None

    return None

