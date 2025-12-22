"""Бенчмарк сортировок для лабораторной работы."""

import random
import time
from typing import Callable, Dict, List

from src.bubble_sort import bubble_sort
from src.bucket_sort import bucket_sort
from src.counting_sort import counting_sort
from src.heap_sort import heap_sort
from src.quick_sort import quicksort
from src.radix_sort import radix_sort
from tests.test_generators import many_duplicates, nearly_sorted, reverse_sorted


def rand_int_array(n: int, lo: int, hi: int, *, seed: int | None = None) -> List[int]:
    if seed is not None:
        random.seed(seed)
    return [random.randint(lo, hi) for _ in range(n)]

def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Измеряет время выполнения одного вызова функции в секундах.
    """
    start = time.perf_counter()
    func(*args, **kwargs)
    end = time.perf_counter()
    return end - start


def quick_sort_wrapper(arr: List[int]) -> List[int]:
    """
    Обёртка для quicksort с границами.
    """
    copied = arr.copy()
    if copied:
        quicksort(copied, 0, len(copied) - 1)
    return copied


def benchmark_sorts(
    arrays: Dict[str, List[int]],
    algos: Dict[str, Callable[[List[int]], List[int]]],
    repeats: int = 3,
) -> Dict[str, Dict[str, float]]:
    """
    Запускает бенчмарк: для каждого алгоритма и каждого массива
    измеряет среднее время выполнения.

    Returns:
        Словарь: {имя_алгоритма: {имя_массива: среднее_время_сек}}
    """
    results: Dict[str, Dict[str, float]] = {}

    for algo_name, algo in algos.items():
        results[algo_name] = {}
        print("=" * 60)
        print(f"Алгоритм: {algo_name}")
        print("=" * 60)

        for arr_name, arr in arrays.items():
            total = 0.0
            for _ in range(repeats):
                data = arr.copy()
                total += timeit_once(algo, data)
            avg = total / repeats
            results[algo_name][arr_name] = avg
            print(f"{arr_name:15}: {avg:.6f} сек")

    return results


def main() -> None:
    n = 10_000

    arrays: Dict[str, List[int]] = {
        "random": rand_int_array(n, -1000, 1000, seed=1),
        "nearly_sorted": nearly_sorted(n, swaps=100, seed=2),
        "duplicates": many_duplicates(n, k_unique=10, seed=3),
        "reverse": reverse_sorted(n),
    }

    algos: Dict[str, Callable[[List[int]], List[int]]] = {
        "bubble_sort": bubble_sort,
        "counting_sort": counting_sort,
        "heap_sort": heap_sort,
        "radix_sort": radix_sort,
        "quicksort": quick_sort_wrapper,
    }

    print("Бенчмарк целочисленных сортировок")
    benchmark_sorts(arrays, algos, repeats=3)

    print("\nБенчмарк bucket_sort (float [0, 1))")
    print("=" * 60)

    float_arrays: Dict[str, List[float]] = {
        "random_float": [random.random() for _ in range(n)],
        "few_values": [random.choice([0.1, 0.2, 0.3, 0.4]) for _ in range(n)],
    }

    bucket_results: Dict[str, Dict[str, float]] = {}
    bucket_results["bucket_sort"] = {}
    for arr_name, arr in float_arrays.items():
        total = 0.0
        for _ in range(3):
            data = arr.copy()
            total += timeit_once(bucket_sort, data)
        avg = total / 3
        bucket_results["bucket_sort"][arr_name] = avg
        print(f"{arr_name:15}: {avg:.6f} сек")


if __name__ == "__main__":
    main()
