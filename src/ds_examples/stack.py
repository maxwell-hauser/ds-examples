class Stack:
    """A simple LIFO stack using a Python list.

    Methods
    -------
    push(item): Add an item to the top of the stack.
    pop(): Remove and return the top item. Raises IndexError if empty.
    peek(): Return the top item without removing. Raises IndexError if empty.
    is_empty(): Return True if the stack is empty.
    size(): Return the number of items in the stack.
    """

    def __init__(self) -> None:
        self._items = []

    def push(self, item) -> None:
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)
