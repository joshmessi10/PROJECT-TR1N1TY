import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(n, container):
    containers = [0] * n
    balls = [0] * n
    j=0
    for element in container:
        containers[j] += sum(element)
        for i in range(len(element)):
            balls[i] += element[i]
        j+=1
    if sorted(containers) == sorted(balls):
        return "Possible"
    else:
        return "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(n, container)

        fptr.write(result + '\n')

    fptr.close()
