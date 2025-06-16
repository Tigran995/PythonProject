import pandas as pd
from typing import List, Dict, Any
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def read_csv(file_path: Path) -> List[Dict[str, Any]]:
    """Читает CSV с транзакциями. Возвращает [] при ошибках."""
    try:
        return pd.read_csv(file_path).to_dict('records')
    except Exception as e:
        logger.error(f"CSV read error: {e}")
        return []


def read_excel(file_path: Path, sheet: str = "Transactions") -> List[Dict[str, Any]]:
    """Читает Excel с транзакциями. Возвращает [] при ошибках."""
    try:
        return pd.read_excel(file_path, sheet_name=sheet).to_dict('records')
    except Exception as e:
        logger.error(f"Excel read error: {e}")
        return []
