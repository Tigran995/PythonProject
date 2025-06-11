import json
from typing import List, Dict, Any
from .logging_config import setup_logger

# Инициализация логера
logger = setup_logger('utils', 'utils.log')


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает JSON-файл и возвращает список словарей с данными о транзакциях.

    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            if isinstance(data, list):
                logger.info(f'Успешно прочитан файл {file_path}. Найдено {len(data)} транзакций')
                return data

            logger.warning(f'Файл {file_path} не содержит список. Возвращен пустой список')
            return []

    except FileNotFoundError:
        logger.error(f'Файл {file_path} не найден')
        return []
    except json.JSONDecodeError:
        logger.error(f'Файл {file_path} содержит невалидный JSON')
        return []