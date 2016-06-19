#!/usr/bin/python3
"""
    This is a simple implementation of Red-Black Tree Node
"""
from TreeNode import Node

class RBTNode(Node):

    def __init__(self, value=None, left=None, right=None, parent=None, coloour=None):
        super().__init__(value, left, right, parent)
        self.colour = colour