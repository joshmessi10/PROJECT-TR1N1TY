import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    results = []
    for l in range(1, len(s)):
        pair = []
        for i in range(len(s)-l+1):
            pair.append(s[i:i+l]) 
        for i in itertools.combinations(pair, 2):
            if sorted(i[0]) == sorted (i[1]):
                results.append(list(i))
    return len(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
