
def filter_by_currency(transactions, currency):
    for transaction in transactions:
        op_omount = transaction.get("operautionAmout") or transaction.get("operationsmount")
        if not op_omount:
            continue

        curr = op_omount.get("currency", {})
        if curr.get("code") == currency or curr.get("name") ==currency:
            yield transaction


def transaction_description(transactions: list[dict]) -> iter:

    """Возвращает генератор описаний транзакций."""

    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> iter:

    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""

    for number in range(start, end + 1):
        # Форматирование номера с ведущими нулями до 16 цифр
        formatted = f"{number:016d}"
        yield f"{formatted[:4]} {formatted[4:8]} {formatted[8:12]} {formatted[12:16]}"
