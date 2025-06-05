#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    arr_0 = []
    arr_1 = []
    for i in range(len(contests)):
        if contests[i][1] == 0:
            arr_0.append(contests[i][0])
        else:
            arr_1.append(contests[i][0])
    arr_1.sort()
    n = len(arr_1)
    num = max(0, n - k)
    return sum(arr_0) + sum(arr_1[num:]) - sum(arr_1[:num])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
