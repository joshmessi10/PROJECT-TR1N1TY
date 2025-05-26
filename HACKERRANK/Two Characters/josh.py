#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    if len(s) == 1:
        return 0
    else:
        comb = list(combinations(set(s),2))
        a = ["" for i in range(len(comb))]  
        for i in s:
            j=0
            for element in comb:
                if i in list(element):
                    a[j] = a[j] + i
                j += 1
    print(a)
    
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
