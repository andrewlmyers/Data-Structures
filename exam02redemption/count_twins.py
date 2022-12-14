#!/usr/bin/env python3

'''
Title:      count_twins.py
Abstract:   Count twins in a binary tree
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       11/21/2022
Questions:

    1. What is the time complexity for count_twins()?

        O(n)

'''

from dataclasses import dataclass

@dataclass
class Node:
    value: int
    left:  'Node'=None
    right: 'Node'=None

def count_twins(node):
    ''' Count twins in a binary tree
                3
             2     2
          4   4   5   6
    >>> tree = Node(3, Node(2, Node(4), Node(4)), Node(2, Node(5), Node(6)))
    >>> count_twins(tree)
    2
    
                3
             2     2
          4   4   7   7
    >>> tree = Node(3, Node(2, Node(4), Node(4)), Node(2, Node(7), Node(7)))
    >>> count_twins(tree)
    3

                3
             3     2
          9   4   5   7
    >>> tree = Node(3, Node(3, Node(9), Node(4)), Node(2, Node(5), Node(7)))
    >>> count_twins(tree)
    0
    '''
    if node is None:
        return 0

    left_twins = count_twins(node.left)
    right_twins = count_twins(node.right)

    if node.left and node.right and (node.left.value == node.right.value):
        has_twins = 1
    else:
        has_twins = 0

    return left_twins + right_twins + has_twins