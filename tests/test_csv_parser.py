import unittest
from unittest.mock import patch, mock_open
from src.file_parsers.csv_parser import parse_csv


class TestCSVParser(unittest.TestCase):
    @patch('builtins.open', mock_open(read_data='id,amount,currency\n1,100,USD'))
    @patch('csv.DictReader')
    def test_parse_csv_success(self, mock_reader):
        mock_reader.return_value = [{'id': '1', 'amount': '100', 'currency': 'USD'}]
        result = parse_csv('dummy.csv')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], '100')
