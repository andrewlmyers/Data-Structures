#!/usr/bin/env python3

'''
Title:      bst_sort.py
Abstract:   Sort an array given in BFS format
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       11/21/2022
Questions:

    1. What type of traversal does this most closely resemble?

        Depth-first traversal (In-order)

    2. What is the time complexity for bst_sort()?

        O(n)
'''

def bst_sort(array, index=0):
    ''' Return an array of sorted values in a binary search tree given in BFS format.
    >>> bst_sort([5, 3, 8, 1, 4, 7, 9])
    [1, 3, 4, 5, 7, 8, 9]
    >>> bst_sort([4, 2, 6, 1, 0, 5, 7])
    [1, 2, 4, 5, 6, 7]
    '''

    if index >= len(array) or array[index] == 0:
        return []

    left_nodes = bst_sort(array, 2*index + 1)
    current_node = [array[index]]
    right_nodes = bst_sort(array, 2*index + 2)

    return left_nodes + current_node + right_nodes