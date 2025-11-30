"""Тесты для пузырьковой сортировки."""

from src.bubble_sort import bubble_sort


class TestBubbleSort:
    """Тесты для bubble_sort."""

    def test_empty_array(self):
        """Тест пустого массива."""
        assert bubble_sort([]) == []

    def test_single_element(self):
        """Тест массива из одного элемента."""
        assert bubble_sort([5]) == [5]

    def test_already_sorted(self):
        """Тест уже отсортированного массива."""
        arr = [1, 2, 3, 4, 5]
        assert bubble_sort(arr.copy()) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Тест массива, отсортированного в обратном порядке."""
        arr = [5, 4, 3, 2, 1]
        assert bubble_sort(arr.copy()) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        """Тест случайного массива."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        assert bubble_sort(arr.copy()) == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self):
        """Тест массива с дубликатами."""
        arr = [5, 2, 8, 2, 9, 1, 5]
        assert bubble_sort(arr.copy()) == [1, 2, 2, 5, 5, 8, 9]

    def test_all_same(self):
        """Тест массива из одинаковых элементов."""
        arr = [7, 7, 7, 7, 7]
        assert bubble_sort(arr.copy()) == [7, 7, 7, 7, 7]

    def test_negative_numbers(self):
        """Тест массива с отрицательными числами."""
        arr = [3, -1, 4, -5, 2]
        assert bubble_sort(arr.copy()) == [-5, -1, 2, 3, 4]

    def test_two_elements(self):
        """Тест массива из двух элементов."""
        assert bubble_sort([2, 1]) == [1, 2]
        assert bubble_sort([1, 2]) == [1, 2]
