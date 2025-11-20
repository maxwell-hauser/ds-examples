class BinaryTree:
    """A minimal Binary Search Tree (BST) supporting insert, find, and traversals.
    """

    class _Node:
        __slots__ = ("key", "left", "right")

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self) -> None:
        self._root = None

    def insert(self, key) -> None:
        def _insert(node, key):
            if node is None:
                return self._Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node

        self._root = _insert(self._root, key)

    def find(self, key) -> bool:
        cur = self._root
        while cur is not None:
            if key == cur.key:
                return True
            cur = cur.left if key < cur.key else cur.right
        return False

    def inorder(self):
        def _in(node):
            if node is None:
                return []
            return _in(node.left) + [node.key] + _in(node.right)

        return _in(self._root)

    def preorder(self):
        def _pre(node):
            if node is None:
                return []
            return [node.key] + _pre(node.left) + _pre(node.right)

        return _pre(self._root)

    def postorder(self):
        def _post(node):
            if node is None:
                return []
            return _post(node.left) + _post(node.right) + [node.key]

        return _post(self._root)
