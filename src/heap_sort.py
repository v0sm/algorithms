"""Модуль для пирамидальной сортировки (heap sort)."""


def heap_sort(arr: list[int]) -> list[int]:
    """
    Сортирует массив методом пирамидальной сортировки.

    Временная сложность: O(n log n) — всегда, даже в худшем случае
    Пространственная сложность: O(1) — сортировка на месте (in-place)

    Args:
        arr: Массив целых чисел для сортировки

    Returns:
        Отсортированный массив (тот же объект, изменённый на месте)
    """
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)

    return arr


def heapify(arr: list[int], heap_size: int, root_index: int) -> None:
    """
    Превращает поддерево с корнем в root_index в max-heap.

    Временная сложность: O(log n)

    Args:
        arr: Массив, представляющий кучу
        heap_size: Размер кучи (количество элементов для рассмотрения)
        root_index: Индекс корня поддерева для heapify

    Returns:
        None
    """
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]

        heapify(arr, heap_size, largest)
