from collections import deque


class Queue:
    """A simple FIFO queue using collections.deque for O(1) operations.

    Methods
    -------
    enqueue(item): Add an item to the back of the queue.
    dequeue(): Remove and return the front item. Raises IndexError if empty.
    peek(): Return the front item without removing. Raises IndexError if empty.
    is_empty(): Return True if the queue is empty.
    size(): Return the number of items in the queue.
    """

    def __init__(self) -> None:
        self._items = deque()

    def enqueue(self, item) -> None:
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)
