class LinkedList:
    """A minimal singly-linked list.

    Supports append, find, and remove (first occurrence).
    """

    class _Node:
        __slots__ = ("value", "next")

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def append(self, value) -> None:
        node = self._Node(value)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self._size += 1

    def find(self, predicate) -> "LinkedList._Node | None":
        cur = self._head
        while cur is not None:
            if predicate(cur.value):
                return cur
            cur = cur.next
        return None

    def remove(self, value) -> bool:
        prev = None
        cur = self._head
        while cur is not None:
            if cur.value == value:
                if prev is None:
                    self._head = cur.next
                else:
                    prev.next = cur.next
                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def __len__(self) -> int:
        return self._size

    def to_list(self):
        out = []
        cur = self._head
        while cur is not None:
            out.append(cur.value)
            cur = cur.next
        return out
