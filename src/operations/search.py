import re
from typing import List, Dict


def search_by_description(operations: List[Dict], search_str: str) -> List[Dict]:
    """
    Ищет операции по строке в описании с использованием регулярных выражений

    Args:
        operations: Список операций
        search_str: Строка для поиска (регистронезависимая)

    Returns:
        Отфильтрованный список операций
    """
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get('description', ''))]
