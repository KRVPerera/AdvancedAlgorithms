#!/usr/bin/python3
"""
    This is a simple implementation of Treap
"""
import os, sys

lib_path = os.path.abspath(os.path.join('..', 'basic'))
sys.path.append(lib_path)

from RBTNode import RBTNode

class RBT(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()