from typing import List, Dict, Union


def parse_excel(file_path: str) -> List[Dict[str, Union[str, float]]]:
    """
    Парсит Excel-файл с транзакциями

    Args:
        file_path: Путь к Excel-файлу (.xlsx)

    Returns:
        Список словарей с транзакциями
    """
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
