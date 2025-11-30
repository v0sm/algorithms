def bubble_sort(array: list[int]) -> list[int]:
    """
    Сортирует массив методом пузырьковой сортировки.

    Временная сложность: O(n^2) — 2 вложенных цикла.
    Лучший случай: O(n) (если массив уже отсортирован).

    Args:
        array: Массив целых чисел для сортировки.
    Returns:
        Отсортированный массив.
    """
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array
