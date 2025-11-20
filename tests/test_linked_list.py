from ds_examples import LinkedList


def test_linked_list_append_find_remove():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.find(lambda v: v == 20) is not None
    assert ll.remove(20) is True
    assert ll.find(lambda v: v == 20) is None
    assert ll.to_list() == [10, 30]
    assert len(ll) == 2
