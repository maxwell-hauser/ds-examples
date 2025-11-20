from ds_examples import Stack


def test_stack_push_pop_peek():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1


def test_stack_empty_errors():
    s = Stack()
    try:
        s.pop()
        assert False, "Expected IndexError"
    except IndexError:
        pass
    try:
        s.peek()
        assert False, "Expected IndexError"
    except IndexError:
        pass
