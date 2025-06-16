from operations.search import search_by_description
from operations.stats import count_by_categories
from utils.file_parsers import read_json_file, read_csv_file, read_excel_file


def main():
    """Основная логика программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор файла
    file_choice = input(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    # Чтение файла
    file_path = input("Введите путь к файлу: ")
    operations = []

    if file_choice == '1':
        operations = read_json_file(file_path)
    elif file_choice == '2':
        operations = read_csv_file(file_path)
    elif file_choice == '3':
        operations = read_excel_file(file_path)

    # Фильтрация по статусу
    while True:
        status = input(
            "Введите статус (EXECUTED/CANCELED/PENDING): "
        ).upper()
        if status in {'EXECUTED', 'CANCELED', 'PENDING'}:
            break
        print(f"Статус операции '{status}' недоступен")

    filtered_ops = [op for op in operations if op.get('status', '').upper() == status]

    # Дополнительные фильтры
    if input("Отсортировать операции по дате? (Да/Нет): ").lower() == 'да':
        reverse = input("По возрастанию или по убыванию? ").lower() == 'по убыванию'
        filtered_ops.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    if input("Выводить только рублевые транзакции? (Да/Нет): ").lower() == 'да':
        filtered_ops = [op for op in filtered_ops if op.get('currency') == 'RUB']

    if input("Фильтровать по слову в описании? (Да/Нет): ").lower() == 'да':
        word = input("Введите слово для поиска: ")
        filtered_ops = search_by_description(filtered_ops, word)

    # Вывод результатов
    if not filtered_ops:
        print("Не найдено подходящих транзакций")
        return

    print(f"Всего операций: {len(filtered_ops)}")
    for op in filtered_ops:
        print(f"{op.get('date')} {op.get('description')}")
        print(f"Сумма: {op.get('amount')} {op.get('currency')}\n")


if __name__ == "__main__":
    main()
