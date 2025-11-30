"""Модуль для вычисления факториала."""


def factorial_recursive(n: int) -> int:
    """
    Вычисляет факториал числа n классическим рекурсивным методом.

    Args:
        n: Неотрицательное целое число

    Returns:
        Факториал числа n

    Raises:
        RecursionError: Если n слишком большое (превышен лимит рекурсии)
    """
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n методом произведения через дерево.

    Временная сложность: O(n log n) - быстрее классической рекурсии для больших n
    Пространственная сложность: O(log n)

    Args:
        n: Неотрицательное целое число

    Returns:
        Факториал числа n
    """
    if n == 0:
        return 1

    def product_range(start: int, end: int) -> int:
        """
        Вычисляет произведение чисел в диапазоне [start, end].

        Args:
            start: Начало диапазона (включительно)
            end: Конец диапазона (включительно)

        Returns:
            Произведение всех чисел от start до end
        """
        if start == end:
            return start
        if end - start == 1:
            return start * end
        mid = (start + end) // 2
        left = product_range(start, mid)
        right = product_range(mid + 1, end)
        return left * right

    return product_range(1, n)
