"""Тесты для блочной сортировки."""

import pytest

from src.bucket_sort import bucket_sort


class TestBucketSort:
    """Тесты для bucket_sort."""

    def test_empty_array(self):
        """Тест пустого массива."""
        assert bucket_sort([]) == []

    def test_single_element(self):
        """Тест массива из одного элемента."""
        assert bucket_sort([0.5]) == [0.5]

    def test_already_sorted(self):
        """Тест уже отсортированного массива."""
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        assert bucket_sort(arr.copy()) == [0.1, 0.2, 0.3, 0.4, 0.5]

    def test_reverse_sorted(self):
        """Тест массива, отсортированного в обратном порядке."""
        arr = [0.9, 0.7, 0.5, 0.3, 0.1]
        assert bucket_sort(arr.copy()) == [0.1, 0.3, 0.5, 0.7, 0.9]

    def test_random_array(self):
        """Тест случайного массива."""
        arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
        result = bucket_sort(arr.copy())
        expected = sorted(arr)
        assert result == expected

    def test_duplicates(self):
        """Тест массива с дубликатами."""
        arr = [0.5, 0.2, 0.5, 0.3, 0.2]
        assert bucket_sort(arr.copy()) == [0.2, 0.2, 0.3, 0.5, 0.5]

    def test_custom_bucket_count(self):
        """Тест с пользовательским количеством корзин."""
        arr = [0.1, 0.5, 0.3, 0.7]
        assert bucket_sort(arr.copy(), buckets=2) == [0.1, 0.3, 0.5, 0.7]

    def test_value_error_negative(self):
        """Тест, что отрицательные числа вызывают ошибку."""
        with pytest.raises(ValueError, match="must be in range"):
            bucket_sort([-0.1, 0.5])

    def test_value_error_greater_than_one(self):
        """Тест, что числа >= 1 вызывают ошибку."""
        with pytest.raises(ValueError, match="must be in range"):
            bucket_sort([0.5, 1.0])

    def test_edge_case_zero(self):
        """Тест граничного случая с нулём."""
        arr = [0.0, 0.5, 0.3]
        assert bucket_sort(arr.copy()) == [0.0, 0.3, 0.5]

    def test_edge_case_almost_one(self):
        """Тест граничного случая с числом близким к 1."""
        arr = [0.99, 0.5, 0.3]
        assert bucket_sort(arr.copy()) == [0.3, 0.5, 0.99]
