#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n):
    if len(n) == 1:
        return int(n)
    else: 
        suma = 0
        for i in range(len(n)):
            suma += int(n[i])
        return superDigit(str(suma))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])
    
    suma = 0
    for i in range(len(n)):
        suma += int(n[i])
    suma *= k
        
    result = superDigit(str(suma))

    fptr.write(str(result) + '\n')

    fptr.close()
