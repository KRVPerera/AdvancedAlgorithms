from unittest import TestCase
from BST import BST

class TestBST(TestCase):
    def test_size_1(self):
        bst = BST()
        bst.insert(20)
        # bst.insert(20)
        self.assertEqual(1, bst.size)

    def test_size_0(self):
        bst = BST()
        self.assertEqual(0, bst.size)

    def test_size_2(self):
        bst = BST()
        bst.insert(20)
        bst.insert(22)
        self.assertEqual(2, bst.size)


    def test_insert(self):
        pass
