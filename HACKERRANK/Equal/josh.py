#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    min_val = min(arr)
    result = float('inf')
    for base in range(min_val, min_val-5,-1):
        operations = 0
        for val in arr:
            diff = val - base
            operations += diff // 5
            diff %= 5
            operations += diff // 2
            diff %= 2
            operations += diff
        result = min(result, operations)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
