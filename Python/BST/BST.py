#!/usr/bin/python3
"""
    This is a simple implementation of BST
    binary search tree
"""
import os, sys

lib_path = os.path.abspath(os.path.join('..', 'basic'))
sys.path.append(lib_path)

from TreeNode import Node


class BST(object):
    # property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
    def __init__(self):
        self.root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    def __len__(self):
        return self._size

    def __iter__(self):
        return self.root.__iter__()

    def insert(self, val):
        if self.root:
            self._insert(val, self.root)
        else:
            self.root = Node(value=val)
        self.size += 1

    def _insert(self, value, currentNode):
        if value <= currentNode.value:
            if currentNode.hasLeftChild():
                self._insert(value, currentNode.left)
            else:
                currentNode.left = Node(value, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._insert(value, currentNode.right)
            else:
                currentNode.right = Node(value, parent=currentNode)
