#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    c = list(Counter(s).values())
    c = sorted(c, reverse=True)
    d = sorted(c)
    if max(c) == min(c):
        return "YES"
    print(c)
    if (c[0] != c[1] and (c[0] -1 == c[1] or c[0] -1 == 0) and c[1] == c[-1]) or (d[0] != d[1] and (d[0] -1 == d[1] or d[0] -1 == 0) and d[1] == d[-1]):
        return "YES"
    return "NO"

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
