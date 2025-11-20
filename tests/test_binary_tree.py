from ds_examples import BinaryTree


def test_binary_tree_insert_find_traversals():
    bt = BinaryTree()
    for n in [7, 3, 9, 1, 5, 8, 10]:
        bt.insert(n)
    assert bt.find(5) is True
    assert bt.find(6) is False
    assert bt.inorder() == [1, 3, 5, 7, 8, 9, 10]
    assert bt.preorder()[0] == 7
    assert bt.postorder()[-1] in {10, 9, 8, 5, 3, 1, 7}
