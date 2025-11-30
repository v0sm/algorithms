"""Тесты для функций вычисления чисел Фибоначчи."""

from src.fibonacci import fibonacci, fibonacci_recursive


class TestFibonacci:
    """Тесты для функций Фибоначчи."""

    def test_fibonacci_zero(self):
        """Тест для n=0."""
        assert fibonacci(0) == 0
        assert fibonacci_recursive(0) == 0

    def test_fibonacci_one(self):
        """Тест для n=1."""
        assert fibonacci(1) == 1
        assert fibonacci_recursive(1) == 1

    def test_fibonacci_small_numbers(self):
        """Тест небольших чисел."""
        assert fibonacci(2) == 1
        assert fibonacci(5) == 5
        assert fibonacci(10) == 55

    def test_fibonacci_medium_numbers(self):
        """Тест средних чисел."""
        assert fibonacci(20) == 6765
        assert fibonacci(30) == 832040

    def test_fibonacci_large_numbers(self):
        """Тест больших чисел (только матричный метод)."""
        assert fibonacci(50) == 12586269025
        assert fibonacci(100) == 354224848179261915075

    def test_fibonacci_consistency_small(self):
        """Тест, что оба метода дают одинаковый результат для малых n."""
        for n in range(15):
            assert fibonacci(n) == fibonacci_recursive(n)
