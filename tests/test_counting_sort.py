"""Тесты для сортировки подсчётом."""

from src.counting_sort import counting_sort


class TestCountingSort:
    """Тесты для counting_sort."""

    def test_empty_array(self):
        """Тест пустого массива."""
        assert counting_sort([]) == []

    def test_single_element(self):
        """Тест массива из одного элемента."""
        assert counting_sort([5]) == [5]

    def test_already_sorted(self):
        """Тест уже отсортированного массива."""
        arr = [1, 2, 3, 4, 5]
        assert counting_sort(arr.copy()) == [1, 2, 3, 4, 5]

    def test_reverse_sorted(self):
        """Тест массива, отсортированного в обратном порядке."""
        arr = [5, 4, 3, 2, 1]
        assert counting_sort(arr.copy()) == [1, 2, 3, 4, 5]

    def test_random_array(self):
        """Тест случайного массива."""
        arr = [4, 2, 2, 8, 3, 3, 1]
        assert counting_sort(arr.copy()) == [1, 2, 2, 3, 3, 4, 8]

    def test_duplicates(self):
        """Тест массива с дубликатами."""
        arr = [5, 2, 8, 2, 9, 1, 5]
        assert counting_sort(arr.copy()) == [1, 2, 2, 5, 5, 8, 9]

    def test_all_same(self):
        """Тест массива из одинаковых элементов."""
        arr = [7, 7, 7, 7, 7]
        assert counting_sort(arr.copy()) == [7, 7, 7, 7, 7]

    def test_negative_numbers(self):
        """Тест массива с отрицательными числами."""
        arr = [3, -1, 4, -5, 2, 0]
        assert counting_sort(arr.copy()) == [-5, -1, 0, 2, 3, 4]

    def test_large_range(self):
        """Тест массива с большим диапазоном значений."""
        arr = [1000, 1, 500, 250, 750]
        assert counting_sort(arr.copy()) == [1, 250, 500, 750, 1000]
