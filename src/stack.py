"""Модуль для реализации структуры данных Stack (стек)."""


class Stack:
    """
    Реализация стека с поддержкой операции min() за O(1).

    Attributes:
        _data: Список для хранения элементов стека
        _min_stack: Вспомогательный стек для отслеживания минимальных элементов
    """

    def __init__(self) -> None:
        """Инициализирует пустой стек."""
        self._data: list[int] = []
        self._min_stack: list[int] = []

    def push(self, value: int) -> None:
        """
        Добавляет элемент на вершину стека.

        Args:
            value: Целое число для добавления в стек
        """
        self._data.append(value)
        if not self._min_stack or value <= self._min_stack[-1]:
            self._min_stack.append(value)

    def pop(self) -> int:
        """
        Удаляет и возвращает элемент с вершины стека.

        Returns:
            Значение удалённого элемента

        Raises:
            IndexError: Если стек пуст
        """
        if not self._data:
            raise IndexError('Stack is empty')

        removed = self._data.pop()
        if removed == self._min_stack[-1]:
            self._min_stack.pop()
        return removed

    def peek(self) -> int:
        """
        Возвращает элемент на вершине стека без удаления.

        Returns:
            Значение элемента на вершине стека

        Raises:
            IndexError: Если стек пуст
        """
        if not self._data:
            raise IndexError('Stack is empty')
        return self._data[-1]

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке за O(1).

        Returns:
            Минимальное значение в стеке

        Raises:
            IndexError: Если стек пуст
        """
        if not self._data:
            raise IndexError('Stack is empty')
        return self._min_stack[-1]

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.

        Returns:
            Количество элементов в стеке
        """
        return len(self._data)
