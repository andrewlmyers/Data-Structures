#!/usr/bin/env python3

'''
Title:      reddit_groups.py
Abstract:   Determine how many isolated groups are in graph.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       11/30/2022
Questions:

    1. Does it make a difference if you used BFS or DFS for walk_graph?
    Explain.

        The way each node is visited is different, but the result will be the same. Since there is no indexing in a 
        dictionary, each key is already initialized, and the dictionary will be the same.

    2. What is the average time complexity of walk_graph?

        O(n) because each node is only visited once and is passed over if found in visited.

    3. What is the average time complexity of find_groups?
        
        O(n) because if a vertex is visited, that group will no longer be checked (i.e. each group is only checked once)
'''

import io
import sys

# Functions

def read_graph(stream=sys.stdin):
    ''' Read one graph from the stream.

    >>> read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    {1: [2, 4], 2: [1, 3], 3: [2], 4: [1]}

    >>> read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    {1: [2], 2: [1], 3: [4], 4: [3]}
    '''
    # Get nvertices and nedges
    try:
        n = int(stream.readline().strip())
    except:
        return None

    try:
        m = int(stream.readline().strip())
    except:
        return None

    # Make graph through dictionary comprehension
    graph = {i:[] for i in range(1, n + 1)}

    # Create adjacency lists
    for _ in range(m):
        source, target = map(int, stream.readline().split())
        graph[source].append(target)
        graph[target].append(source)

    return graph


def walk_graph(graph, origin):
    ''' Perform traversal of graph from origin.

    >>> g = read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    >>> walk_graph(g, 1)
    {1, 2, 3, 4}

    >>> g = read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    >>> walk_graph(g, 1)
    {1, 2}
    '''
    # Vertices we can vist
    frontier = [origin]
    # Vertices we have already visited
    visited = set()

    while frontier:
        vertex = frontier.pop()

        # Continue if vertex already seen
        if vertex in visited:
            continue
        
        # Add current vertex
        visited.add(vertex)

        # Adding neighbors to frontier list
        for neighbor in graph[vertex]:
            frontier.append(neighbor)

    return visited
    

def find_groups(graph):
    ''' Find isolated groups in graph.

    >>> g = read_graph(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n'))
    >>> find_groups(g)
    [[1, 2, 3, 4]]

    >>> g = read_graph(io.StringIO('4\\n2\\n1 2\\n3 4\\n'))
    >>> find_groups(g)
    [[1, 2], [3, 4]]
    '''
    # Groups to be returned
    groups = []
    # Number of vertices as a reference
    num_vertices = len(graph)
    # Visited vertices set
    visited = set()
    # Iterator through vertices
    origin = 0

    while True:
        origin += 1

        if origin in visited:
            continue

        # Add all neighbors to visited list; all will be in the same group
        temp = walk_graph(graph, origin)
        for node in temp:
            visited.add(node)

        # Add group to groups list
        groups.append(list(temp))
        # All vertices accounted for
        if len(visited) == num_vertices: break

    return groups

# Main Execution

def main(stream=sys.stdin):
    ''' For each graph, find the number of isolated graphs, and print them out
    in sorted order.

    >>> main(io.StringIO('4\\n3\\n1 2\\n2 3\\n4 1\\n4\\n2\\n1 2\\n3 4\\n10\\n8\\n1 2\\n6 8\\n8 1\\n10 6\\n7 7\\n7 5\\n3 6\\n6 2\\n'))
    Graph 1:
    1 2 3 4
    Graph 2:
    1 2
    3 4
    Graph 3:
    1 2 3 6 8 10
    4
    5 7
    9
    '''
    i = 1
    while graph := read_graph(stream):
        # Initializing groups
        groups = find_groups(graph)
        print("Graph", str(i) + ":")
        
        # Print out each group
        for group in groups:
            temp = map(str, group)
            string = " ".join(temp)
            print(string)

        # Iterate for printing the graph number
        i += 1

if __name__ == '__main__':
    main()
