"""Тесты для структуры данных Stack."""

import pytest

from src.stack import Stack


class TestStack:
    """Тесты для класса Stack."""

    def test_init_empty(self):
        """Тест создания пустого стека."""
        stack = Stack()
        assert len(stack) == 0

    def test_push_single(self):
        """Тест добавления одного элемента."""
        stack = Stack()
        stack.push(5)
        assert len(stack) == 1
        assert stack.peek() == 5

    def test_push_multiple(self):
        """Тест добавления нескольких элементов."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert len(stack) == 3
        assert stack.peek() == 3

    def test_pop_single(self):
        """Тест удаления единственного элемента."""
        stack = Stack()
        stack.push(5)
        value = stack.pop()
        assert value == 5
        assert len(stack) == 0

    def test_pop_multiple(self):
        """Тест удаления нескольких элементов."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert len(stack) == 0

    def test_pop_empty_raises_error(self):
        """Тест, что pop из пустого стека вызывает ошибку."""
        stack = Stack()
        with pytest.raises(IndexError, match="Stack is empty"):
            stack.pop()

    def test_peek_empty_raises_error(self):
        """Тест, что peek из пустого стека вызывает ошибку."""
        stack = Stack()
        with pytest.raises(IndexError, match="Stack is empty"):
            stack.peek()

    def test_min_single_element(self):
        """Тест min для стека с одним элементом."""
        stack = Stack()
        stack.push(5)
        assert stack.min() == 5

    def test_min_multiple_elements(self):
        """Тест min для стека с несколькими элементами."""
        stack = Stack()
        stack.push(5)
        stack.push(3)
        stack.push(7)
        stack.push(1)
        assert stack.min() == 1

    def test_min_after_pop(self):
        """Тест min после удаления минимального элемента."""
        stack = Stack()
        stack.push(5)
        stack.push(3)
        stack.push(7)
        stack.push(1)
        assert stack.min() == 1
        stack.pop()
        assert stack.min() == 3
        stack.pop()
        assert stack.min() == 3
        stack.pop()
        assert stack.min() == 5

    def test_min_with_duplicates(self):
        """Тест min с дубликатами минимального значения."""
        stack = Stack()
        stack.push(5)
        stack.push(2)
        stack.push(2)
        stack.push(7)
        assert stack.min() == 2
        stack.pop()
        assert stack.min() == 2
        stack.pop()
        assert stack.min() == 2
        stack.pop()
        assert stack.min() == 5

    def test_min_empty_raises_error(self):
        """Тест, что min из пустого стека вызывает ошибку."""
        stack = Stack()
        with pytest.raises(IndexError, match="Stack is empty"):
            stack.min()

    def test_peek_does_not_modify(self):
        """Тест, что peek не изменяет стек."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert len(stack) == 2
        assert stack.peek() == 2

    def test_len_operations(self):
        """Тест правильности len при различных операциях."""
        stack = Stack()
        assert len(stack) == 0
        stack.push(1)
        assert len(stack) == 1
        stack.push(2)
        assert len(stack) == 2
        stack.pop()
        assert len(stack) == 1
        stack.pop()
        assert len(stack) == 0
