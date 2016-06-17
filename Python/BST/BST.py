#!/usr/bin/python3
"""
    This is a simple implementation of BST
    binary search tree
"""
from node import Node


class BST(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, value):
        if self.root:
            self._put(value, self.root)
        else:
            self.root = Node(value == value)

    def _insert(self, value, currentNode):
        if value < currentNode.value:
            if currentNode.hasLeftChild():
                self._insert(value, currentNode.leftChild)
            else:
                currentNode.leftChild = Node(value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(value, currentNode.rightChild)
            else:
                currentNode.rightChild = Node(value, parent=currentNode)
