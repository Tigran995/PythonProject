import pytest
from datetime import datetime
from processing import filter_by_state, sort_by_date

# Фикстура с тестовыми данными
@pytest.fixture
def sample_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01T12:00:00"},
        {"id": 2, "state": "CANCELLED", "date": "2023-09-15T08:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-05T15:45:00"},
        {"id": 4, "date": "2023-11-20T10:10:00"}  # Отсутствует state
    ]

# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELLED", 1),
    ("PENDING", 0)
])
def test_filter_by_state(sample_operations, state, expected_count):
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count
    for item in result:
        assert item.get("state") == state

# Тесты для sort_by_date
@pytest.mark.parametrize("reverse, expected_order", [
    (True, ["2023-11-20", "2023-10-05", "2023-10-01", "2023-09-15"]),
    (False, ["2023-09-15", "2023-10-01", "2023-10-05", "2023-11-20"])
])
def test_sort_by_date(sample_operations, reverse, expected_order):
    # Удаляем элемент без state для чистоты теста
    operations = [op for op in sample_operations if "date" in op]
    sorted_ops = sort_by_date(operations, reverse=reverse)
    sorted_dates = [op["date"].split("T")[0] for op in sorted_ops]
    assert sorted_dates == expected_order

# Тест на некорректные даты
def test_invalid_date_format():
    operations = [{"date": "2023-13-01T00:00:00"}]  # Неверный месяц
    with pytest.raises(ValueError):
        sort_by_date(operations)
