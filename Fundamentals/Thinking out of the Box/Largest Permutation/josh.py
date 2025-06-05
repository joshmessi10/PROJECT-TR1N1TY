#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestPermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def largestPermutation(k, arr):
    n = len(arr)
    positions = {value: idx for idx, value in enumerate(arr)}
    for i in range(n):
        value = n-i
        if arr[i] == value:
            continue
        if k==0:
            break
        index = positions[value]
        positions[value] = i
        positions[arr[i]] = index
        
        arr[i], arr[index] = arr[index], arr[i]
        k-=1
        
    return arr
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
