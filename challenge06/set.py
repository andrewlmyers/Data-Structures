#!/usr/bin/env python3

'''
Title:      set.py
Abstract:   Implement a Set using a binary search tree.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questions:

    1. What is the average time complexity insert()?

        O(logh) h is the height of the tree
    
    2. What is the worst-case time complexity insert()?

        O(h) h is the height of the tree

    3. What is the base case for the _insert() and _search() methods?

        The best case is when the node being insertd is the root and when the node
        being searched for is the root.
'''

from dataclasses import dataclass

# Classes

@dataclass
class Node:
    ''' Simple Node with string key and int value. '''
    value:  int
    left:   'Node'=None
    right:  'Node'=None

class Set:
    ''' Simple Set Implementation based on a binary search tree. '''

    def __init__(self):
        ''' Initialize empty set.

        >>> s = Set(); not s.root
        True
        '''
        self.root = None

    def insert(self, value):
        ''' Insert value pair into set.

        Test tree:

                 5
               /   \
              4     7
             /       \
            1         9

        >>> s = Set()
        >>> s.insert(5); s.root.value
        5

        >>> s.insert(7); s.root.right.value
        7

        >>> s.insert(4); s.root.left.value
        4

        >>> s.insert(9); s.root.right.right.value
        9

        >>> s.insert(1); s.root.left.left.value
        1
        '''
        # Try to insert to set; if match is found then nothing is changed
        try:
            self.root = self._insert(self.root, value)
        except ValueError:
            pass
    
    def _insert(self, node, value):
        ''' Insert value into set (recursive). '''
        # Base case: Non-existent Node
        if node is None:
            return Node(value)

        # Base case: Found match
        if value == node.value:
            raise ValueError

        # Recursive: Go to left or right subtree based on value
        if value <= node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        # return the node to relink the set
        return node

    def search(self, value):
        ''' Return whether or not value is in set.

        >>> s = Set()
        >>> for n in [5, 7, 4, 9, 1]: s.insert(n)
        >>> all(s.search(n) for n in [5, 7, 4, 9, 1])
        True

        >>> any(s.search(n) for n in [0, 3, 8, 10])
        False
        '''
        return self._search(self.root, value)
    
    def _search(self, node, value):
        ''' Return whether or not value is in set (recursive). '''
        # Base case: Non-existent node
        if node is None:
            return False

        # Base case: Found Match
        if value == node.value:
            return True

        # Recursive: Go to left or right subtree based on value
        if value <= node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
