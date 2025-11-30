"""Модуль для быстрой сортировки с разбиением Хоара."""


def swap(array: list[int], i: int, j: int) -> None:
    """
    Меняет местами два элемента массива.

    Args:
        array: Массив для операции
        i: Индекс первого элемента
        j: Индекс второго элемента
    """
    array[i], array[j] = array[j], array[i]


def hoare_partition(array: list[int], left: int, right: int) -> int:
    """
    Выполняет разбиение массива по схеме Хоара.

    Временная сложность: O(n).

    Args:
        array: Массив для разбиения
        left: Левая граница диапазона (включительно)
        right: Правая граница диапазона (включительно)

    Returns:
        Индекс разделения, после которого начинается правая часть.
    """
    pivot = array[(right + left) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        swap(array, i, j)


def quicksort(array: list[int], left: int, right: int) -> list[int]:
    """
    Сортирует массив методом быстрой сортировки с разбиением Хоара.

    Временная сложность:
        - Средний случай: O(n log n)
        - Худший случай: O(n^2) (редко при выборе pivot из середины)
    Пространственная сложность: O(log n) — стек рекурсивных вызовов.

    Args:
        array: Массив целых чисел для сортировки
        left: Левая граница диапазона сортировки (обычно 0)
        right: Правая граница диапазона сортировки (обычно len(array) - 1)

    Returns:
        Отсортированный массив.
    """
    if left < right:
        partition_index = hoare_partition(array, left, right)
        quicksort(array, left, partition_index)
        quicksort(array, partition_index + 1, right)
    return array
