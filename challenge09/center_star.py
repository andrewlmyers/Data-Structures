#!/usr/bin/env python3

'''
Title:      center_star.py
Abstract:   Determine center of star graph.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       11/30/2022
Questions:

    1. If you did not use a defaultdict to represent the graph, how else could
    you have added the edges to the adjaceny list (describe one alternative
    approach)?

        You could use a normal dictionary and check if a key exists. If not, initialize key value with an empty list; if so, add node to list.

    2. What is the average time complexity of find_center?

        O(n) because it is essentially a liner search, comparing each keys' value length by iterating through the keys.
'''

import io
import sys

from collections import defaultdict

# Functions

def read_graph(stream=sys.stdin):
    ''' Read one graph from the stream.

    >>> read_graph(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n'))
    defaultdict(<class 'list'>, {1: [2], 2: [1, 3, 4], 3: [2], 4: [2]})

    >>> read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n1 4\\n'))
    defaultdict(<class 'list'>, {1: [2, 5, 3, 4], 2: [1], 5: [1], 3: [1], 4: [1]})

    >>> read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n2 4\\n'))
    defaultdict(<class 'list'>, {1: [2, 5, 3], 2: [1, 4], 5: [1], 3: [1], 4: [2]})
    '''
    graph = defaultdict(list)

    # get number of edges from stream
    try:
        m = int(stream.readline().strip())
    except:
        # if there is not a number, or the end of the list of graphs is reached, return None
        return None

    # adding adjacency lists to vertexes
    for _ in range(m):
        source, target = map(int, stream.readline().split())
        graph[source].append(target)
        graph[target].append(source)

    return graph

def find_center(graph):
    ''' Find center vertex of star graph.

    >>> find_center(read_graph(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n')))
    2

    >>> find_center(read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n1 4\\n')))
    1

    >>> find_center(read_graph(io.StringIO('4\\n1 2\\n5 1\\n1 3\\n2 4\\n')))
    '''
    # star value is when the number of neighbors is equal to n - 1, where n is number of nodes
    star = len(graph) - 1

    # if the length of adjacency list is equal to star value, return node value
    for key in graph.keys():
        if len(graph[key]) == star:
            return key
    
    return None

# Main Execution

def main(stream=sys.stdin):
    ''' For each graph, determine which vertex is the center of the star graph,
    and print it out.

    >>> main(io.StringIO('3\\n1 2\\n2 3\\n4 2\\n4\\n1 2\\n5 1\\n1 3\\n1 4\\n4\\n1 2\\n5 1\\n1 3\\n2 4\\n'))
    Vertex 2 is the center
    Vertex 1 is the center
    There is no center
    '''
    # read input stream
    while graph := read_graph(stream):
        center = find_center(graph)
        if center:
            print("Vertex", str(center), "is the center")
        else:
            print("There is no center")



if __name__ == '__main__':
    main()
