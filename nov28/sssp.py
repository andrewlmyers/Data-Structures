#!/usr/bin/env python3

''' sssp.py
Example of Dijkstra's algorithm for single source shortest path.
'''

import collections
import heapq
import sys

# Build Graph

def read_graph():
    ''' Read in directed graph '''
    graph = collections.defaultdict(dict)
    for line in sys.stdin:
        source, target, weight = line.split()
        graph[source][target] = int(weight)
    return graph

# Compute SSSP

def compute_sssp(graph, start):
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    frontier = []
    visited  = {}

    heapq.heappush(frontier, (0, start))

    while frontier:
        distance, vertex = heapq.heappop(frontier)

        if vertex in visited:
            continue

        visited[vertex] = distance

        for neighbor, weight in graph[vertex].items():
            heapq.heappush(frontier, (distance + weight, neighbor))

    return visited

# Main Execution

def main():
    # Read Graph
    graph   = read_graph()

    # Compute SSSP
    start   = min(graph.keys())
    visited = compute_sssp(graph, start)

    # Display Distances
    for target in sorted((graph.keys()))[1:]:
        print(f'{start} -> {target} = {visited[target]}')

if __name__ == '__main__':
    main()