"""Модуль для поразрядной сортировки (radix sort)."""


def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    """
    Сортирует массив целых чисел методом поразрядной сортировки.

    Временная сложность: O(d * (n + k)), где:
        - n — количество элементов
        - d — максимальное количество разрядов
        - k — основание системы счисления (base)
    Пространственная сложность: O(n + k)

    Args:
        arr: Массив целых чисел для сортировки
        base: Основание системы счисления (по умолчанию 10)

    Returns:
        Отсортированный массив
    """
    if not arr:
        return arr

    negative = [abs(x) for x in arr if x < 0]
    positive = [x for x in arr if x >= 0]

    if negative:
        negative = radix_sort_positive(negative, base)
        negative = [-x for x in reversed(negative)]  # переворачиваем и делаем отрицательными

    if positive:
        positive = radix_sort_positive(positive, base)

    return negative + positive


def radix_sort_positive(arr: list[int], base: int = 10) -> list[int]:
    """
    Сортирует массив неотрицательных целых чисел поразрядной сортировкой.

    Args:
        arr: Массив неотрицательных целых чисел
        base: Основание системы счисления

    Returns:
        Отсортированный массив
    """
    if not arr:
        return arr

    max_val = max(arr)
    num_digits = 0
    temp = max_val
    while temp > 0:
        temp //= base
        num_digits += 1

    if num_digits == 0:
        num_digits = 1

    exp = 1
    for _ in range(num_digits):
        arr = counting_sort_by_digit(arr, exp, base)
        exp *= base

    return arr

def counting_sort_by_digit(arr: list[int], exp: int, base: int) -> list[int]:
    """
    Выполняет сортировку подсчётом по определённому разряду.

    Args:
        arr: Массив целых чисел для сортировки
        exp: Позиция разряда (1 для единиц, 10 для десятков, 100 для сотен и т.д.)
        base: Основание системы счисления (количество возможных цифр)

    Returns:
        Массив, отсортированный по указанному разряду
    """
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for num in arr:
        digit = (num // exp) % base
        count[digit] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        num = arr[i]
        digit = (num // exp) % base
        output[count[digit] - 1] = num
        count[digit] -= 1

    return output
