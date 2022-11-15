#!/usr/bin/env python3

'''
Title:      duplicates.py
Abstract:   Determine whether or not a line of words contains any duplicates.
Author:     Andrew Myers
Email:      amyers9@nd.edu
Estimate:   30 minutes
Date:       10/31/2022
Questions:

    1. What is the average time complexity of detect_duplicates()?

        O(nlogh)

    2. What is the worst-case time complexity of detect_duplicates()?

        O(n^2)

    3. What is the worst-case space complexity of detect_duplicates()?

        O(n^2)

    4. How would you modify the program to make it case in-sensitive?

        Before turning the line into a set, you can convert each char
        to lower case and then make the set.
'''

from operator import truediv
import sys

from set import Set

# Functions

def detect_duplicates(words):
    ''' Return whether or not the sequence of words contains a duplicate.

    >>> detect_duplicates('a b c'.split())
    False

    >>> detect_duplicates('a b a'.split())
    True

    >>> detect_duplicates('a b c b e f'.split())
    True
    '''
    # initialize set with only first word (no duplicates possible at this point)
    s = Set()
    s.insert(words[0])

    # for loop searches for duplicate, if none found, add word to set and continue
    for i in range(1, len(words)):
        contains = s.search(words[i])
        if contains:
            return True
        s.insert(words[i])

    # return false if true was not returned in loop
    return False

# Main Execution

def main(stream=sys.stdin):
    ''' For each line of words, determine if there are any duplicates.

    >>> import io
    >>> main(io.StringIO('a b c\\na b a\\na b c b e f\\n'))
    False
    True
    True
    '''
    for line in stream:
        print(detect_duplicates(line.split()))

if __name__ == '__main__':
    main()
