import unittest
from operations.stats import count_by_categories


class TestStats(unittest.TestCase):
    def test_category_counting(self):
        ops = [{'description': 'A'}, {'description': 'B'}, {'description': 'A'}]
        result = count_by_categories(ops, ['A', 'B'])
        self.assertEqual(result, {'A': 2, 'B': 1})
