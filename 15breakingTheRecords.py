#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    breaking_high_count = breaking_low_count = 0
    highest_score = lowest_score = scores[0]

    for score in scores[1:]:
        if score > highest_score:
            breaking_high_count += 1
            highest_score = score

        if score < lowest_score:
            breaking_low_count += 1
            lowest_score = score

    return breaking_high_count, breaking_low_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
