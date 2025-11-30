"""Модуль для сортировки подсчётом (counting sort)."""


def counting_sort(array: list[int]) -> list[int]:
    """
    Сортирует массив методом сортировки подсчётом.

    Временная сложность: O(n + k), где n — размер массива, k — диапазон значений
    Пространственная сложность: O(k) — для массива подсчётов.

    Args:
        array: Массив целых чисел для сортировки

    Returns:
        Отсортированный массив.
    """
    if len(array) <= 1:
        return array

    min_val = min(array)
    max_val = max(array)

    count = [0] * (max_val - min_val + 1)

    for num in array:
        count[num - min_val] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            array[index] = i + min_val
            index += 1
            count[i] -= 1

    return array
