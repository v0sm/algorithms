"""Тесты для пирамидальной сортировки."""

from src.heap_sort import heap_sort


class TestHeapSort:
    """Тесты для heap_sort."""

    def test_empty_array(self):
        """Тест пустого массива."""
        assert heap_sort([]) == []

    def test_single_element(self):
        """Тест массива из одного элемента."""
        assert heap_sort([5]) == [5]

    def test_already_sorted(self):
        """Тест уже отсортированного массива."""
        arr = [1, 2, 3, 4, 5]
        assert heap_sort(arr.copy()) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Тест массива, отсортированного в обратном порядке."""
        arr = [5, 4, 3, 2, 1]
        assert heap_sort(arr.copy()) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        """Тест случайного массива."""
        arr = [12, 11, 13, 5, 6, 7]
        assert heap_sort(arr.copy()) == [5, 6, 7, 11, 12, 13]

    def test_duplicates(self):
        """Тест массива с дубликатами."""
        arr = [5, 2, 8, 2, 9, 1, 5]
        assert heap_sort(arr.copy()) == [1, 2, 2, 5, 5, 8, 9]

    def test_all_same(self):
        """Тест массива из одинаковых элементов."""
        arr = [7, 7, 7, 7, 7]
        assert heap_sort(arr.copy()) == [7, 7, 7, 7, 7]

    def test_negative_numbers(self):
        """Тест массива с отрицательными числами."""
        arr = [3, -1, 4, -5, 2]
        assert heap_sort(arr.copy()) == [-5, -1, 2, 3, 4]

    def test_large_array(self):
        """Тест большого массива."""
        arr = list(range(100, 0, -1))
        result = heap_sort(arr.copy())
        assert result == list(range(1, 101))
