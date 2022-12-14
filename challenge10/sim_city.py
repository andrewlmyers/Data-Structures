#!/usr/bin/env python3

'''
Title:      sim_city.py
Abstract:   Compute the minimum spanning tree of points in a city map.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       12/7/2022
Questions:

    1. What is the average time complexity of build_graph?

        O(n^2)

    2. What is the average time complexity of compute_mst?

        O(V + ElogE)

    3. What is the average space complexity of compute_mst?

        O(V)

    4. Does the total cost of the minimum spanning tree change if we use
    different starting vertices isfor compute_mst?  Experiment and then
    explain.

        No, the total cost does not change with a different starting vertex.
'''

import collections
import heapq
import io
import math
import requests
import sys

# Constants

POINTS_URL  = 'https://yld.me/raw/jpIx'
POINTS_TEXT = requests.get(POINTS_URL).text

# Read Points

def read_points(stream=sys.stdin):
    ''' Read points from stream.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 2.0, 4.0)]

    >>> read_points(points_stream)
    [(0, 1.0, 1.0), (1, 2.0, 2.0), (2, 1.0, 2.0), (3, 2.0, 1.0)]

    >>> read_points(points_stream)
    [(0, 0.0, 1.0), (1, 2.0, 3.0), (2, 4.0, 1.0), (3, 1.0, 2.0), (4, 5.0, 2.0)]
    '''
    # Read n number of points
    try:
        n = int(stream.readline().strip())
    except:
        return None

    points = []

    # Add points in a tuple to list
    for i in range(n):
        x, y = map(float, stream.readline().split())
        points.append((i, x, y))

    return points


# Build Graph

def build_graph(points):
    ''' Build adjacency list from list of points.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 3.1622776601683795}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 2.0}, 2: {0: 3.1622776601683795, 1: 2.0, 2: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 1.4142135623730951, 2: 1.0, 3: 1.0}, 1: {0: 1.4142135623730951, 1: 0.0, 2: 1.0, 3: 1.0}, 2: {0: 1.0, 1: 1.0, 2: 0.0, 3: 1.4142135623730951}, 3: {0: 1.0, 1: 1.0, 2: 1.4142135623730951, 3: 0.0}})

    >>> build_graph(read_points(points_stream))
    defaultdict(<class 'dict'>, {0: {0: 0.0, 1: 2.8284271247461903, 2: 4.0, 3: 1.4142135623730951, 4: 5.0990195135927845}, 1: {0: 2.8284271247461903, 1: 0.0, 2: 2.8284271247461903, 3: 1.4142135623730951, 4: 3.1622776601683795}, 2: {0: 4.0, 1: 2.8284271247461903, 2: 0.0, 3: 3.1622776601683795, 4: 1.4142135623730951}, 3: {0: 1.4142135623730951, 1: 1.4142135623730951, 2: 3.1622776601683795, 3: 0.0, 4: 4.0}, 4: {0: 5.0990195135927845, 1: 3.1622776601683795, 2: 1.4142135623730951, 3: 4.0, 4: 0.0}})
    '''
    # Initialize graph
    graph = collections.defaultdict(dict)


    # Calculate distance from target to source with distance formula
    for i in range(len(points)):
        for j in range(len(points)):
            source = points[i]
            target = points[j]
            x = (target[1] - source[1]) ** 2
            y = (target[2] - source[2]) ** 2
            graph[source[0]][target[0]] = (x + y) ** 0.5

    return graph


# Compute MST

def compute_mst(graph, start):
    ''' Compute minimum spanning tree.

    >>> points_stream = io.StringIO(POINTS_TEXT)

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 1: 0, 2: 1}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 2: 0, 1: 2, 3: 0}

    >>> graph = build_graph(read_points(points_stream))
    >>> compute_mst(graph, min(graph))
    {0: 0, 3: 0, 1: 3, 2: 1, 4: 2}
    '''
    frontier = [(0, start, start)] # Vertices we can visit
    visited = {}                   # Vertices we have already visited

    while frontier:
        weight, target, source = heapq.heappop(frontier)

        if target in visited: continue # Check if already in visited
        visited[target] = source       # Store optimal distance

        for neighbor, weight in graph[target].items(): # Add neighbors to frontier
            heapq.heappush(frontier, (weight, neighbor, target))

    return visited


# Main Execution

def main(stream=sys.stdin):
    ''' For each set of points, build the graph, compute the MST, and then
    print out the total cost.

    >>> main(io.StringIO(POINTS_TEXT))
    Graph 1: 3.41
    Graph 2: 3.00
    Graph 3: 7.07
    Graph 4: 12.73
    Graph 5: 27.08
    '''
    # Iterator
    i = 1

    # While graphs still exist in the file
    while points := read_points(stream):
        cost = 0
        graph = build_graph(points)
        mst = compute_mst(graph, min(graph))

        # Sum all costs for shortest distances
        for target, source in mst.items():
            cost += graph[source][target]
        print(f"Graph {i}: {cost:.2f}")
        i += 1



if __name__ == '__main__':
    main()
