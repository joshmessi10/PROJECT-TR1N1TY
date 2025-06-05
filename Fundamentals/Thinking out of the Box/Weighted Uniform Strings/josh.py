#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    weights = {chr(i + 96): i for i in range(1, 27)}
    arr = []
    prev = ''
    count = 0
    
    for i in s:
        if i != prev:
            count = 1
            prev = i
        else:
            count += 1
        arr.append(weights.get(i)*count)
    weight_set = set(arr)
    result = ["Yes" if q in weight_set else "No" for q in queries]
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
