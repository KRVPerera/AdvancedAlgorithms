#!/usr/bin/python3
"""
    This is a simple implementation of BST
    binary search tree
"""
from TreeNode import Node

class TreapNode(Node):

    def __init__(self, value=None, left=None, right=None, parent=None, priority=None):
        super().__init__(value, left, right, parent)
        self.priority = priority