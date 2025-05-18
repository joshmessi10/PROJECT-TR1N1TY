import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(x):
    if x == 0: 
        return 0
    answer = 1
    while x > 0:
        answer *= x
        x = x - 1
    return answer

if __name__ == '__main__':
    n = int(input().strip())
    print(extraLongFactorials(n))
