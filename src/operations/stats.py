from collections import Counter
from typing import List, Dict


def count_by_categories(operations: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает операции по категориям

    Args:
        operations: Список операций
        categories: Список категорий для подсчета

    Returns:
        Словарь {категория: количество}
    """
    descriptions = [op.get('description', '') for op in operations]
    return {cat: count for cat, count in Counter(descriptions).items() if cat in categories}
