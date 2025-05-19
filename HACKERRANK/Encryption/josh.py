#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    length = math.sqrt(len(s))
    rows = math.floor(length)
    columns = math.ceil(length)
    if rows * columns < len(s):
        rows = columns
    c = 0
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            try:
                matrix[i][j] = s[c]
            except:
                matrix[i][j] = ""
            c+=1
    res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    result = ""
    for i in range(columns):
        for j in range(rows):
            result = result + res[i][j]
        result = result + " "
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
