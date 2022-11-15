#!/usr/bin/env python3

'''
Title:      cups.py
Abstract:   Determine the minimum amount of time require to fill all cups of water.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questions:

    1. What is the worst-case time complexity of fill_cups()?

        O(nlogn)

    2. What is the worst-case space complexity of fill_cups()?

        O(nlogn)

    3. Why is this considered a greedy approach?

        This is a greedy approach because the most optimal solution is considered at each 
        iteration and not the most optimal for the entire algorithm
'''

import sys

from priority_queue import PriorityQueue

# Functions

def fill_cups(cups):
    ''' Return minimum number of seconds required to fill all cups of water.

    Use a greedy algorithm by attempting to fill two types of cups at a time
    until there is only one remaining type.
    >>> fill_cups([1, 4, 2])
    4

    >>> fill_cups([5, 4, 4])
    7

    >>> fill_cups([5, 0, 0])
    5
    '''
    # initialize the priority queue
    pq = PriorityQueue(cups)

    # initialize 
    seconds = 0
    iter = 1

    # greedy algorithm 
    while pq.data[0] != 0:
        # advancing to non-zero cup for second "pour"
        while pq.data[iter] == 0:
            if iter < len(pq.data) - 1:
                iter += 1
            else: 
                break

        # incrementing each value
        pq.data[0] += 1
        if pq.data[iter] != 0: pq.data[iter] += 1

        # making temp list to make new priority queue
        temp = []
        for num in pq.data:
            temp.append(num * -1)
        seconds += 1
        pq = PriorityQueue(temp)
        temp = 1

    return seconds

# Main Execution

def main(stream=sys.stdin):
    ''' For each line of cups, determine the minimum number of seconds required
    to fill all cups of water.

    >>> import io
    >>> main(io.StringIO('1 4 2\\n5 4 4\\n5 0 0\\n'))
    4
    7
    5
    '''
    # taking input
    for line in stream:
        line_list = line.split()
        ints = [int(num) for num in line_list]
        print(fill_cups(ints))

if __name__ == '__main__':
    main()
