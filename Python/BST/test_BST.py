from unittest import TestCase
import os, sys
import random
lib_path = os.path.abspath(os.path.join('..', 'basic'))
sys.path.append(lib_path)

from BST import BST
from TreeWalk import inorderTreeWalk

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

    def test_inorder_traversal(self):
        bst = BST()
        listi = [x for x in range(50)]
        random.shuffle(listi)
        for j in listi:
            bst.insert(j)

        inorderTreeWalk(bst.root)
        self.assertEqual(len(listi), bst.size)

