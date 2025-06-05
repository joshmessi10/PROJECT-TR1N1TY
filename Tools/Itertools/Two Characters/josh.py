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
    if len(s) == 1 or len(set(s)) == 1:
        return 0
    else:
        comb = list(combinations(set(s),2))
        array = ["" for i in range(len(comb))]  
        for letter in s:
            j=0
            for element in comb:
                if letter in list(element) :
                    array[j] = array[j] + letter
                j += 1
    length = [1 for x in range(len(array))]
    for x in range(len(array)):
        for y in range(len(array[x])-1):
            if array[x][y] != array[x][y+1]:
                length[x] +=1
            else:
                length[x] = 0
                break
    return max(length)
        
        
    return max([len(x)-1 for x in array])
    
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
