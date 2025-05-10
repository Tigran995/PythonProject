from typing import List, Dict

def filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    """
    return [item for item in data if item.get('state') == state]

def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате (ключ 'date').

    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)