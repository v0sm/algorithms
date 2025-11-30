"""Модуль для вычисления чисел Фибоначчи."""


def fibonacci_recursive(n: int) -> int:
    """
    Вычисляет n-е число Фибоначчи классическим рекурсивным методом.

    Временная сложность: O(2^n) - экспоненциальная
    Пространственная сложность: O(n) - глубина рекурсии

    Args:
        n: Порядковый номер числа Фибоначчи (неотрицательное целое)

    Returns:
        n-е число Фибоначчи
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci(n: int) -> int:
    """
    Вычисляет n-е число Фибоначчи матричным методом с быстрым возведением в степень.

    Временная сложность: O(log n)
    Пространственная сложность: O(log n)

    Args:
        n: Порядковый номер числа Фибоначчи (неотрицательное целое)

    Returns:
        n-е число Фибоначчи
    """
    if n <= 1:
        return n

    def matrix_mult(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        """
        Умножает две матрицы 2×2.

        Args:
            a: Первая матрица 2×2
            b: Вторая матрица 2×2

        Returns:
            Результат умножения матриц a и b
        """
        return [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    def matrix_power(m: list[list[int]], power: int) -> list[list[int]]:
        """
        Возводит матрицу 2×2 в степень power методом быстрого возведения.

        Использует алгоритм деления степени пополам для ускорения.

        Args:
            m: Матрица 2×2
            power: Неотрицательная степень

        Returns:
            Матрица m в степени power
        """
        if power == 1:
            return m
        if power % 2 == 0:
            half = matrix_power(m, power // 2)
            return matrix_mult(half, half)
        else:
            return matrix_mult(m, matrix_power(m, power - 1))

    result = matrix_power([[1, 1], [1, 0]], n)
    return result[0][1]
