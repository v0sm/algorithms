"""Тесты для функций вычисления факториала."""

from src.factorial import factorial, factorial_recursive


class TestFactorial:
    """Тесты для функций факториала."""

    def test_factorial_zero(self):
        """Тест факториала нуля."""
        assert factorial(0) == 1
        assert factorial_recursive(0) == 1

    def test_factorial_one(self):
        """Тест факториала единицы."""
        assert factorial(1) == 1
        assert factorial_recursive(1) == 1

    def test_factorial_small_numbers(self):
        """Тест факториала небольших чисел."""
        assert factorial(5) == 120
        assert factorial_recursive(5) == 120
        assert factorial(6) == 720
        assert factorial_recursive(6) == 720

    def test_factorial_medium_numbers(self):
        """Тест факториала средних чисел."""
        assert factorial(10) == 3628800
        assert factorial_recursive(10) == 3628800

    def test_factorial_large_numbers(self):
        """Тест факториала больших чисел."""
        result = factorial(20)
        expected = 2432902008176640000
        assert result == expected

    def test_factorial_consistency(self):
        """Тест, что оба метода дают одинаковый результат."""
        for n in range(15):
            assert factorial(n) == factorial_recursive(n)
