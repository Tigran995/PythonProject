from unittest.mock import patch
import pytest
from src.external_api import convert_to_rub


@patch('src.external_api.requests.get')
def test_convert_to_rub(mock_get):
    # Тест для RUB
    transaction = {'amount': '100', 'currency': 'RUB'}
    assert convert_to_rub(transaction) == 100.0

    # Тест для USD с моком API
    mock_response = type('MockResponse', (), {
        'json': lambda self: {'rates': {'RUB': 75.5}},
        'raise_for_status': lambda self: None
    })
    mock_get.return_value = mock_response()

    transaction = {'amount': '10', 'currency': 'USD'}
    assert convert_to_rub(transaction) == 755.0

    # Тест для ошибки API
    mock_get.side_effect = Exception('API error')
    assert convert_to_rub(transaction) is None
