import os
from PythonProject.src.decorators import log
import pytest


@pytest.fixture
def log_file():
    """Фикстура для тестов с файлом логов"""
    filename = "test_log.txt"
    yield filename
    # Удаляем файл после теста
    if os.path.exists(filename):
        os.remove(filename)


def test_log_to_file(log_file):
    """Тест записи логов в файл"""

    @log(filename=log_file)
    def add(a, b):
        return a + b

    # Вызываем функцию
    assert add(2, 3) == 5

    # Проверяем содержимое файла
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "add ok" in content


def test_log_error_to_file(log_file):
    """Тест записи ошибок в файл"""

    @log(filename=log_file)
    def divide(a, b):
        return a / b

    # Вызываем функцию с ошибкой
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Проверяем содержимое файла
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "divide error: ZeroDivisionError" in content
        assert "Inputs: (1, 0), {}" in content


def test_log_to_console(capsys):
    """Тест вывода логов в консоль"""

    @log()
    def multiply(a, b):
        return a * b

    # Вызываем функцию
    assert multiply(2, 3) == 6

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "multiply ok" in captured.out


def test_log_error_to_console(capsys):
    """Тест вывода ошибок в консоль"""

    @log()
    def fail():
        raise ValueError("Test error")

    # Вызываем функцию с ошибкой
    with pytest.raises(ValueError):
        fail()

    # Проверяем вывод в консоль
    captured = capsys.readouterr()
    assert "fail error: ValueError" in captured.out