#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def commonChild(s1, s2):
    dp = [[0 for i in range(len(s1)+1)] for _ in range(len(s2)+1)]
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            #print(f"i: {i}, j: {j}\n")
            if s1[i-1] == s2[j-1]:
                #print(f"s1: {s1[i-1]}, s2: {s2[j-1]}\n")
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #print(dp)
    return dp[len(s1)][len(s2)]
    
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
