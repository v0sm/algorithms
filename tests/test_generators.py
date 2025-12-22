"""Модуль генерации тест-кейсов и проверки сортировок."""

import random
from typing import Dict, List

from src.bubble_sort import bubble_sort
from src.bucket_sort import bucket_sort
from src.counting_sort import counting_sort
from src.heap_sort import heap_sort
from src.quick_sort import quicksort
from src.radix_sort import radix_sort


def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed: int | None = None) -> List[int]:
    """Случайный массив целых чисел."""
    if seed is not None:
        random.seed(seed)
    if distinct:
        nums = random.sample(range(lo, hi + 1), min(n, hi - lo + 1))
        return nums[:n] if n < len(nums) else nums
    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed: int | None = None) -> List[int]:
    """Почти отсортированный массив."""
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(n: int, k_unique: int = 5, *, seed: int | None = None) -> List[int]:
    """Массив с малым количеством уникальных значений."""
    if seed is not None:
        random.seed(seed)
    unique_vals = list(range(k_unique))
    return [random.choice(unique_vals) for _ in range(n)]


def reverse_sorted(n: int) -> List[int]:
    """Обратно отсортированный массив."""
    return list(range(n - 1, -1, -1))


def test_all_sorts() -> Dict[str, Dict[str, bool]]:
    """Тестирует все сортировки на разных типах данных."""
    def quick_sort_wrapper(arr: List[int]) -> List[int]:
        arr_copy = arr.copy()
        if arr_copy:
            quicksort(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    sorts = {
        "bubble_sort": bubble_sort,
        "counting_sort": counting_sort,
        "heap_sort": heap_sort,
        "radix_sort": radix_sort,
        "quicksort": quick_sort_wrapper,
    }

    test_cases = {
        "empty": [],
        "single": [42],
        "small": [64, 34, 25, 12, 22, 11, 90],
        "random": rand_int_array(20, -50, 50, seed=1),
        "nearly_sorted": nearly_sorted(20, 5, seed=2),
        "duplicates": many_duplicates(20, k_unique=5, seed=3),
        "reverse": reverse_sorted(10),
        "negative": [-5, 3, -10, 0, 7, -2],
    }

    results: Dict[str, Dict[str, bool]] = {}

    for sort_name, sort_func in sorts.items():
        print("=" * 50)
        print(f"Тестируем {sort_name}")
        print("=" * 50)

        results[sort_name] = {}
        all_passed = True

        for case_name, data in test_cases.items():
            expected = sorted(data)
            result = sort_func(data.copy())
            passed = (result == expected)
            results[sort_name][case_name] = passed

            status = "OK" if passed else "FAIL"
            preview = data[:5]
            suffix = "..." if len(data) > 5 else ""
            print(f"{case_name:15} | {preview}{suffix} -> {status}")

            if not passed:
                all_passed = False
                print(f"  Ожидалось: {expected}")
                print(f"  Получено:  {result}")

        print(f"Итог для {sort_name}: {'ВСЕ ТЕСТЫ ПРОЙДЕНЫ' if all_passed else 'ЕСТЬ ОШИБКИ'}")

    print("=" * 50)
    print("Тестируем bucket_sort")
    print("=" * 50)

    float_tests = []

    float_tests.append(([], []))

    inp = [0.42, 0.32, 0.33, 0.52, 0.37]
    float_tests.append((inp, sorted(inp)))

    inp = [0.1, 0.2, 0.3, 0.4]
    float_tests.append((inp, sorted(inp)))

    inp = [0.5, 0.5, 0.5]
    float_tests.append((inp, sorted(inp)))

    random.seed(10)
    inp = [random.random() for _ in range(20)]
    float_tests.append((inp, sorted(inp)))

    for i, (inp, expected) in enumerate(float_tests):
        result = bucket_sort(inp.copy())
        status = "OK" if result == expected else "FAIL"
        preview = inp[:5]
        suffix = "..." if len(inp) > 5 else ""
        print(f"bucket test {i}: {preview}{suffix} -> {status}")
        if status == "FAIL":
            print(f"  Ожидалось: {expected}")
            print(f"  Получено:  {result}")

    return results


if __name__ == "__main__":
    print("Генерация тест-кейсов и автотестирование")
    print("=" * 60)

    print("\nПримеры генерации:")
    print("rand_int_array(5, 1, 10):", rand_int_array(5, 1, 10, seed=4))
    print("nearly_sorted(5, 1):", nearly_sorted(5, 1, seed=5))
    print("many_duplicates(5):", many_duplicates(5, seed=6))
    print("reverse_sorted(5):", reverse_sorted(5))

    test_all_sorts()
