import logging
from pathlib import Path


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """
    Настраивает и возвращает логер для модуля.

    Args:
        name: Имя логера (обычно __name__ модуля)
        log_file: Имя файла для записи логов

    Returns:
        Настроенный логер
    """
    # Создаем папку logs, если ее нет
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Очищаем существующие handlers
    if logger.handlers:
        logger.handlers.clear()

    # Настраиваем file handler
    file_handler = logging.FileHandler(
        filename=logs_dir / log_file,
        mode='w',  # Перезаписываем файл при каждом запуске
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)

    # Настраиваем форматтер
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
