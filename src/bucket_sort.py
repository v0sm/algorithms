"""Модуль для блочной сортировки (bucket sort)."""
from src.bubble_sort import bubble_sort


def bucket_sort(arr: list[float], buckets: int = None) -> list[float]:
    """
    Bucket sort для float чисел в диапазоне [0, 1).

    Args:
        arr: список float чисел в диапазоне [0, 1)
        buckets: количество корзин (по умолчанию = len(arr))

    Returns:
        Отсортированный список
    """
    if not arr:
        return arr

    if buckets is None:
        buckets = len(arr)

    if any(x < 0 or x >= 1 for x in arr):
        raise ValueError("All elements must be in range [0, 1)")

    bucket_list = [[] for _ in range(buckets)]

    for num in arr:
        index = int(num * buckets)
        if index >= buckets:
            index = buckets - 1
        bucket_list[index].append(num)

    for i in range(buckets):
        bubble_sort(bucket_list[i])

    result = []
    for bucket in bucket_list:
        result.extend(bucket)

    return result
