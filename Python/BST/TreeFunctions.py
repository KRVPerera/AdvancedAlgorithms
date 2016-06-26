#!/usr/bin/python3
"""
    This is a simple implementation of BST
    binary search tree
"""

def inorderTreeWalk(node):
    if node is not None:
        inorderTreeWalk(node.left)
        print(node, end=" ")
        inorderTreeWalk(node.right)

def treeSearch(node, val):
    # print(node.value)
    if node == None or node.value == val:
        return node
    if val < node.value:
        return treeSearch(node.left, val)
    else:
        return treeSearch(node.right, val)

def treeSearchIter(node, val):
    while node is not None and val != node.value:
        if val < node.value:
            node = node.left
        else:
            node = node.left
    return node

def treeMin(node):
    while node.hasLeftChild():
        node = node.left
    return node

def treeMinRecursive(node):
    if not node.hasLeftChild():
        return node
    return treeMinRecursive(node.left)


def treeMax(node):
    while node.hasRightChild():
        node = node.right
    return node

def treeMaxRecursive(node):
    if not node.hasRightChild():
        return node
    return treeMaxRecursive(node.right)

def treeSuccessor(node):
    if node.hasRightChild():
        return treeMin(node.right)
    y = node.parent
    while y is not None and node == y.right:
        node = y
        y = y.parent
    return y

def treePredecessor(node):
    if node.hasLeftChild():
        return treeMax(node.left)
    y = node.parent
    while y is not None and node == y.left:
        node = y
        y = y.parent
    return y

def treeInsert(tree, node):
    y = None
    x = tree.root
    while x is not None:
        y = x
        if node.value < x.value:
            x = x.left
        else:
            x = x.right

    node.parent = y
    if y is None:
        tree.root = node
    elif node.value < y.value:
        y.left = node
    else:
        node.right = node
    tree.size += 1

def treeTransplant(tree, sbtree_u, sbtree_v):
    if sbtree_u.parent is None:
        tree.root = sbtree_v
    elif sbtree_u == sbtree_u.parent.left:
        sbtree_u.parent.left = sbtree_v
    else:
        sbtree_u.parent.right = sbtree_v
    if sbtree_v is not None:
        sbtree_v.parent = sbtree_u.parent

def treeDelete(tree, node):
    if not node.hasLeftChild():
        treeTransplant(tree, node, node.right)
    elif not node.hasRightChild():
        treeTransplant(tree, node, node.left)
    else:
        y = treeMin(node.right)  #y = treeSuccessor(node)
        if node != y.parent:
            treeTransplant(tree, y, y.right)
            y.right = node.right
            y.right.parent = y
        treeTransplant(tree, node, y)
        y.left = node.left
        y.left.parent = y



