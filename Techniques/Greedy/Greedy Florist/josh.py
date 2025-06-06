#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort(reverse=True)
    w=k
    counter = 0
    total = 0
    for i in range(len(c)):
        if w > 0:
            total += (counter+1) * c[i] 
            w-= 1
        if w == 0:
            counter += 1
            w = k
    return total  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
