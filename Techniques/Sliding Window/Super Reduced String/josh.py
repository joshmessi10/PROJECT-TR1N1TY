#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    s2 = list(s)
    flag = False
    i=0
    while not flag:
        try:
            if s2[i] == s2[i+1]:
                s2.pop(i+1)
                s2.pop(i)
                i=0
            else:
                i = i+1
        except IndexError:
            flag = True
         
    result = "".join(s2)
    if result == "":
        return "Empty String"
    return result
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
