#!/usr/bin/python3
"""
    This is a simple implementation of Red-Black Tree Node
"""
from enum import Enum
from TreeNode import Node


class Colour(Enum):
    black = 0
    red = 1

class RBTNode(Node):

    def __init__(self, value=None, left=None, right=None, parent=None, colour=Colour.black):
        super().__init__(value, left, right, parent)
        self.colour = colour