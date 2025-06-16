import csv
from typing import List, Dict, Union


def parse_csv(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Парсит CSV-файл с транзакциями

    Args:
        file_path: Путь к CSV-файлу

    Returns:
        Список словарей с транзакциями
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except (FileNotFoundError, csv.Error) as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []
