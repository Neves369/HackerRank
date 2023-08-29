#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Initialize the counters
    count_apples = 0
    count_oranges = 0

    # Iterate through the list of apples
    for apple in apples:
        # Check if the apple falls within Sam's house
        if s <= a + apple <= t:
            count_apples += 1

    # Iterate through the list of oranges
    for orange in oranges:
        # Check if the orange falls within Sam's house
        if s <= b + orange <= t:
            count_oranges += 1

    # Print the number of apples and oranges
    print(count_apples)
    print(count_oranges)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
