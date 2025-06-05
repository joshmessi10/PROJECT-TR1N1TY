#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    for i in range(len(s)//2):
        print(f"a: {s[i]}, b: {s[i+1]}, c: {s[i-2]}, d: {s[i-1]}")
        if abs(ord(s[i+1]) - ord(s[i])) !=  abs(ord(s[len(s)-1 - i]) - ord(s[len(s)-2-i])):
            return "Not Funny"
    return "Funny"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
