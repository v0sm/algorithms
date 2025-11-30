"""Тесты для поразрядной сортировки."""

from src.radix_sort import radix_sort


class TestRadixSort:
    """Тесты для radix_sort."""

    def test_empty_array(self):
        """Тест пустого массива."""
        assert radix_sort([]) == []

    def test_single_element(self):
        """Тест массива из одного элемента."""
        assert radix_sort([5]) == [5]

    def test_already_sorted(self):
        """Тест уже отсортированного массива."""
        arr = [1, 12, 123, 1234, 12345]
        assert radix_sort(arr.copy()) == [1, 12, 123, 1234, 12345]

    def test_reverse_sorted(self):
        """Тест массива, отсортированного в обратном порядке."""
        arr = [500, 400, 300, 200, 100]
        assert radix_sort(arr.copy()) == [100, 200, 300, 400, 500]

    def test_random_array(self):
        """Тест случайного массива."""
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        assert radix_sort(arr.copy()) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_duplicates(self):
        """Тест массива с дубликатами."""
        arr = [121, 432, 564, 23, 1, 45, 788, 23]
        assert radix_sort(arr.copy()) == [1, 23, 23, 45, 121, 432, 564, 788]

    def test_negative_numbers(self):
        """Тест массива с отрицательными числами."""
        arr = [170, -45, 75, -90, 2, 0]
        assert radix_sort(arr.copy()) == [-90, -45, 0, 2, 75, 170]

    def test_only_negative(self):
        """Тест массива только из отрицательных чисел."""
        arr = [-5, -2, -8, -1]
        assert radix_sort(arr.copy()) == [-8, -5, -2, -1]

    def test_different_bases(self):
        """Тест с разными основаниями."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        assert radix_sort(arr.copy(), base=2) == [11, 12, 22, 25, 34, 64, 90]
        assert radix_sort(arr.copy(), base=16) == [11, 12, 22, 25, 34, 64, 90]
