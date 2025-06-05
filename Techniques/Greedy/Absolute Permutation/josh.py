#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    arr = []
    for i in range(1,n+1):
        arr.append(i)  
    if k == 0:
        return arr   
    if n % (2*k) != 0:
        return [-1]
    result = []
    shift = True
    for i in range(1,n+1):
        if shift:
            result.append(i+k)
        else:
            result.append(i-k)
        if i % k == 0:
            shift = not shift
    return result
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
