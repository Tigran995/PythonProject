from unittest.mock import patch, mock_open
import pytest
import pandas as pd
from src.file_reader import read_csv_file, read_excel_file


@pytest.fixture
def mock_csv_data():
    return """id,amount,currency
1,100,RUB
2,200,USD
"""

from unittest.mock import patch, MagicMock
from pathlib import Path
from src.file_reader import read_csv, read_excel

@patch('pandas.read_csv')
def test_csv_reader(mock_read):
    mock_read.return_value = MagicMock(to_dict=lambda: [{"id": 1}])
    assert read_csv(Path("test.csv")) == [{"id": 1}]

@patch('pandas.read_excel')
def test_excel_reader(mock_read):
    mock_read.return_value = MagicMock(to_dict=lambda: [{"id": 2}])
    assert read_excel(Path("test.xlsx")) == [{"id": 2}]
