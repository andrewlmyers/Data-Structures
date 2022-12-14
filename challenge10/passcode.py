#!/usr/bin/env python3

'''
Title:      passcode.py
Abstract:   Use topological sort to crack the passcode.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       12/7/2022
Questions:

    1. What does compute_degrees produce?

        Compute degrees produces the number of edges connecting to that vertex. By setting each key's degree to zero initially, 
        it esentially makes a directed graph to help solve the password with Kahn's algorithm.

    2. What is the average time complexity of compute_degrees?

        O(V + E)

    3. What is the average time complexity of topological sort?

        O(V + E)

    4. What is the average space complexity of topological sort?

        O(V)
'''

import collections
import io
import sys

# Constants

SAMPLE_CODES = [352, 154, 542, 315, 152]
LONGER_CODES = [219, 183, 804, 376, '043', 904, 357, 857, 206, 180, 983, 284, 843]

# Functions

def read_graph(stream=sys.stdin):
    ''' Read codes into graph (adjacency set).

    >>> read_graph(io.StringIO('\\n'.join(map(str, SAMPLE_CODES))))
    defaultdict(<class 'set'>, {3: {1, 5}, 5: {2, 4}, 1: {5}, 4: {2}})

    >>> read_graph(io.StringIO('\\n'.join(map(str, LONGER_CODES))))
    defaultdict(<class 'set'>, {2: {0, 1, 8}, 1: {8, 9}, 8: {0, 3, 4, 5}, 0: {4, 6}, 3: {5, 7}, 7: {6}, 4: {3}, 9: {0, 8}, 5: {7}})
    '''
    # Initialize graph
    graph = collections.defaultdict(set)

    # Read each code and store adjacent values into an adjacency set
    while code := stream.readline().strip():
        graph[int(code[0])].add(int(code[1]))
        graph[int(code[1])].add(int(code[2]))

    return graph

def compute_degrees(graph):
    ''' Compute degrees of all vertices in graph.

    >>> compute_degrees(read_graph(io.StringIO('\\n'.join(map(str, SAMPLE_CODES)))))
    defaultdict(<class 'int'>, {3: 0, 1: 1, 5: 2, 2: 2, 4: 1})

    >>> compute_degrees(read_graph(io.StringIO('\\n'.join(map(str, LONGER_CODES)))))
    defaultdict(<class 'int'>, {2: 0, 0: 3, 1: 1, 8: 3, 9: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2})
    '''
    degrees = collections.defaultdict(int)

    # For each target in source, increment target's degrees by one
    for source, targets in graph.items():
        degrees[source]
        for target in targets:
            degrees[target] += 1

    return degrees

def topological_sort(graph):
    ''' Perform a topological sort on graph.

    >>> topological_sort(read_graph(io.StringIO('\\n'.join(map(str, SAMPLE_CODES)))))
    [3, 1, 5, 4, 2]

    >>> topological_sort(read_graph(io.StringIO('\\n'.join(map(str, LONGER_CODES)))))
    [2, 1, 9, 8, 0, 4, 3, 5, 7, 6]
    '''
    degrees  = compute_degrees(graph)
    frontier = [v for v, d in degrees.items() if d == 0] # Add all 0 degree vertices to frontier
    visited  = []

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        # Decrement each neighbor's degrees and if the neighbor reaches 0 degrees, add to frontier
        for neighbor in graph[vertex]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited


# Main Execution

def main(stream=sys.stdin):
    ''' Read graph from passcodes, perform topological sort, and print original
    full passcode.

    >>> main(io.StringIO('\\n'.join(map(str, SAMPLE_CODES))))
    31542

    >>> main(io.StringIO('\\n'.join(map(str, LONGER_CODES))))
    2198043576
    '''
    graph = read_graph(stream)
    vertices = topological_sort(graph)
    
    string = map(str, vertices)

    print(''.join(string))

if __name__ == '__main__':
    main()
