
import unittest
from unittest.mock import patch, MagicMock
from src.external_api import convert_to_rub
from src.utils import load_transactions


class TestCurrencyConversion(unittest.TestCase):
    @patch('requests.get')
    def test_usd_conversion(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'rates': {'RUB': 75.50}}
        mock_get.return_value = mock_response

        transaction = {'amount': 100, 'currency': 'USD'}
        result = convert_to_rub(transaction)
        self.assertAlmostEqual(result, 7550.0)


class TestJsonLoading(unittest.TestCase):
    @patch('builtins.open')
    def test_load_transactions(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 1}]'
        result = load_transactions('dummy.json')
        self.assertEqual(len(result), 1)

