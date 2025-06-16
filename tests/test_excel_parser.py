import unittest
from unittest.mock import patch
from src.file_parsers.excel_parser import parse_excel


class TestExcelParser(unittest.TestCase):
    @patch('pandas.read_excel')
    def test_parse_excel_success(self, mock_read):
        mock_read.return_value = pd.DataFrame([{'id': 1, 'amount': 100}])
        result = parse_excel('dummy.xlsx')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['amount'], 100)
