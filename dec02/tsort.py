#!/usr/bin/env python3

''' tsort.py
Use Kahn's algorithm to perform a topological sort on a Makefile.
'''

import collections
import sys

# Functions

def read_graph():
    graph = collections.defaultdict(set)

    for line in sys.stdin:
        if ':' not in line:
            continue

        targets, sources = line.split(':', 1)
        targets = targets.split()
        sources = sources.split()

        for source in sources:
            graph[source].update(targets)

    return graph

def compute_degrees(graph):
    degrees = collections.defaultdict(int)

    for source, targets in graph.items():
        degrees[source]
        for target in targets:
            degrees[target] += 1

    return degrees

def topological_sort(graph):
    degrees  = compute_degrees(graph)
    frontier = [v for v, d in degrees.items() if d == 0]
    visited  = []

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        for neighbor in graph[vertex]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited

# Main Execution

def main():
    graph    = read_graph()
    vertices = topological_sort(graph)

    if len(vertices) == len(graph):
        print(' '.join(vertices))
    else:
        print('There is a cycle!')

if __name__ == '__main__':
    main()