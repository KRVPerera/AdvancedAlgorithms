#!/usr/bin/python3
"""
    This is a simple implementation of BST
    binary search tree
"""

def inorderTreeWalk(node):
    if node is not None:
        inorderTreeWalk(node.leftChild)
        print(node, end=" ")
        inorderTreeWalk(node.rightChild)