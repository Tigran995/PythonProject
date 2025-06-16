import unittest
from operations.search import search_by_description


class TestSearch(unittest.TestCase):
    def test_search_case_insensitive(self):
        ops = [{'description': 'Payment'}, {'description': 'Refund'}]
        result = search_by_description(ops, 'payment')
        self.assertEqual(len(result), 1)
