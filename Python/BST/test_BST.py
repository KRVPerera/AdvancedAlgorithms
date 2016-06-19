from unittest import TestCase
import os, sys
lib_path = os.path.abspath(os.path.join('..', 'basic'))
sys.path.append(lib_path)

import random
from BST import BST
from TreeFunctions import *
from TreeNode import Node

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

    def test_Search(self):
        bst = BST()
        listi = [x for x in range(50)]
        random.shuffle(listi)
        for j in listi:
            bst.insert(j)
        searchValue = 40
        inorderTreeWalk(bst.root)
        node = treeSearch(bst.root, searchValue)
        self.assertIsNotNone(node)
        self.assertEqual(searchValue, node.value)

    def test_Search_Iter(self):
        bst = BST()
        listi = [x for x in range(50)]
        random.shuffle(listi)
        for j in listi:
            bst.insert(j)

        node = treeSearch(bst.root, 32)
        self.assertIsNotNone(node)
        self.assertEqual(32, node.value)

    def test_treeSuccessor(self):
        bst = BST()
        listi = [x for x in range(50)]
        random.shuffle(listi)
        for j in listi:
            bst.insert(j)

        nodeSearch = treeSearch(bst.root, 32)
        self.assertIsNotNone(nodeSearch)
        node = treeSuccessor(nodeSearch)
        self.assertIsNotNone(node)
        self.assertEqual(33, node.value)

    def test_treePredecessor(self):
        bst = BST()
        listi = [x for x in range(50)]
        random.shuffle(listi)
        for j in listi:
            bst.insert(j)

        nodeSearch = treeSearch(bst.root, 32)
        self.assertIsNotNone(nodeSearch)
        node = treePredecessor(nodeSearch)
        self.assertIsNotNone(node)
        self.assertEqual(31, node.value)


    def test_MinMax_Recursive(self):
        bst = BST()
        listi = [x for x in range(50)]
        random.shuffle(listi)
        for j in listi:
            bst.insert(j)
        node = treeMinRecursive(bst.root)
        node2 = treeMaxRecursive(bst.root)
        self.assertIsNotNone(node)
        self.assertEqual(0, node.value)
        self.assertIsNotNone(node2)
        self.assertEqual(49, node2.value)

    def test_Insert_Node(self):
        bst = BST()
        tNode1 = Node(21)
        tNode2 = Node(20)
        treeInsert(bst, tNode1)
        treeInsert(bst, tNode2)
        self.assertEqual(2, len(bst))
        searched = treeSearch(bst.root, 20)
        self.assertIsNotNone(searched)

    def test_Delete_Node(self):
        bst = BST()
        treeInsert(bst, Node(21))
        treeInsert(bst,Node(20))
        treeInsert(bst,Node(35))
        treeInsert(bst,Node(64))
        treeInsert(bst,Node(32))

        self.assertEqual(5, len(bst))
        searched = treeSearch(bst.root, 20)
        self.assertIsNotNone(searched)
        treeDelete(bst, searched)
        searchAgain = treeSearch(bst.root, 20)
        self.assertIsNone(searchAgain)
