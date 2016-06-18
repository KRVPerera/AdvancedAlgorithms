from unittest import TestCase
from BST import BST

class TestBST(TestCase):
    def test_size(self):
        bst = BST()
        bst.insert(20)
        bst.insert(20)
        self.assertEqual(2, bst.size)

    def test_insert(self):
        pass
