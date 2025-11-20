from . import Stack, Queue, LinkedList, BinaryTree


def main() -> None:
    print("== Stack Demo ==")
    s = Stack()
    for i in [1, 2, 3]:
        s.push(i)
    print("Popped:", s.pop())  # 3
    print("Top now:", s.peek())  # 2

    print("\n== Queue Demo ==")
    q = Queue()
    for c in ["a", "b", "c"]:
        q.enqueue(c)
    print("Dequeued:", q.dequeue())  # a
    print("Front now:", q.peek())  # b

    print("\n== LinkedList Demo ==")
    ll = LinkedList()
    for x in [10, 20, 30]:
        ll.append(x)
    ll.remove(20)
    print("Values:", ll.to_list())  # [10, 30]

    print("\n== BinaryTree Demo ==")
    bt = BinaryTree()
    for n in [7, 3, 9, 1, 5, 8, 10]:
        bt.insert(n)
    print("Find 5:", bt.find(5))  # True
    print("Inorder:", bt.inorder())  # [1,3,5,7,8,9,10]


if __name__ == "__main__":
    main()
