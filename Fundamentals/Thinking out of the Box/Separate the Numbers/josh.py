#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    if len(s) == 1:
        print("NO")
    for i in range(len(s)//2):
        num = int(s[:i+1])
        new = str(num)
        j=1
        while len(new) < len(s):
            new = new + str(num+j)
            j+=1
        #print(f"i: {i}, New: {new}")
        if new == s:   
            print("YES "+str(num))
            break
        elif i == len(s)//2-1:
            print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
