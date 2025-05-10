# Обработка банковских операций

## Цель
Фильтрация и сортировка данных о банковских операциях.

## Установка
1. Убедитесь, что установлен Python 3.8+.
2. Склонируйте репозиторий.
3. Импортируйте функции из модуля `processing`.

## Использование
### Фильтрация по статусу
```python
from processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELLED', 'date': '2023-01-02'}
]
result = filter_by_state(data, 'CANCELLED')
# Результат: [{'id': 2, 'state': 'CANCELLED', 'date': '2023-01-02'}]
