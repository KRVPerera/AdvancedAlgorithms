#!/usr/bin/python3
"""
    This is a simple implementation of Treap
"""
import os, sys

lib_path = os.path.abspath(os.path.join('..', 'basic'))
sys.path.append(lib_path)

from RBTNode import RBTNode

class RBT(object):
    def getsize(self): return self._size
    def setsize(self, value): self._size = value

    def __init__(self):
        self._nil = RBTNode()
        self._size = 0

    nil = property(fget=lambda self: self._nil, doc="The tree's nil node")
    size = property(fget=getsize, fset=setsize, doc="The size of the tree")

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def treeLeftRotate(self, node):
        assert(node.hasRightChild())
        assert(node.parent == self.nil)
        y = node.right
        node.right = y.left
        if y.left is not self.nil:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == self.nil:
            self.root = y
        elif node.parent.left == node:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def treeInsertNode(self, node):
        pass