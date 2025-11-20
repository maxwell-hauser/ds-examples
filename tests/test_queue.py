from ds_examples import Queue


def test_queue_enqueue_dequeue_peek():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"


def test_queue_empty_errors():
    q = Queue()
    try:
        q.dequeue()
        assert False, "Expected IndexError"
    except IndexError:
        pass
    try:
        q.peek()
        assert False, "Expected IndexError"
    except IndexError:
        pass
