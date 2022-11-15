#!/usr/bin/env python3

'''
Title:      priority_queue.py
Abstract:   Implement a priority queue using a binary heap.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questions:

    1. What is the worst-case time complexity of PriorityQueue.push()?

        O(nlogn)

    2. What is the worst-case time complexity of PriorityQueue.pop()?

        O(nlogn)

    3. How did you work around the fact that heapq is a min-heap, while our
    PriorityQueue is a max-heap?

        By making the original values negative, the largest positive values become the largest
        negative, thus they are the smallest. This achieves priority queue functionality because
        the "largest" number is the root and can be popped easily.
'''

import heapq

# Classes

class PriorityQueue:
    ''' Simple priority queue based on a binary heap. '''

    def __init__(self, data=None):
        ''' Initialize the internal data.

        >>> pq = PriorityQueue(); pq.data
        []

        >>> pq = PriorityQueue([3, 1, 4]); pq.data[0]
        -4
        '''
        # initialize the queue data as an empty list
        self.data = []

        # if user passes list, add the negative of each number to queue data (implementing priority queue with min-queue)
        if data:
            for num in data:
                self.data.append(num * -1)

        # heapifying the negative values puts the greatest absolute value at the front of the queue which is the desired functionality
        heapq.heapify(self.data)

    def push(self, item):
        ''' Add item to Priority Queue.

        >>> pq = PriorityQueue(); pq.push(3); pq.data[0]
        -3

        >>> pq.push(1); pq.data[0]
        -3

        >>> pq.push(4); pq.data[0]
        -4
        '''
        # push the negative of desired value to maintain priority queue structure with min-queue
        heapq.heappush(self.data, item * -1)

    def pop(self):
        ''' Remove and return smallest value from the Priority Queue.
        >>> pq = PriorityQueue([3, 1 ,4]); pq.pop()
        4

        >>> pq.pop()
        3

        >>> pq.pop()
        1
        '''
        # return the negative of the "smallest" value so user gets original value from list
        return heapq.heappop(self.data) * -1

    def size(self):
        ''' Return number of values in Priority Queue.

        >>> pq = PriorityQueue(); pq.size()
        0

        >>> pq = PriorityQueue([3, 1, 4]); pq.size()
        3
        '''
        return len(self.data)