#!/usr/bin/python3
"""
    This is a simple implementation of BST
    binary search tree
"""


class Node(object):
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def isLeaf(self):
        """
            Check whether the node is leaf node or not
        :return: True or False depend on whether a leaf node
        """
        return not (self.rightChild or self.leftChild)

    def isRoot(self):
        """
            Check whether the node has a parent or not
        :return: return True if there is no parent, False if there is a parent
        """
        return not self.parent

    def hasLeftChild(self):
        """
            Check whether the node has a left child or not
        """
        return self.leftChild

    def hasRightChild(self):
        """
            Check whether the node has a right child or not
        """
        return self.rightChild

    def hasAnyChildren(self):
        """
            Check whether the node has any child nodes
            similar to the isLeaf
        """
        return self.rightChild or self.leftChild
