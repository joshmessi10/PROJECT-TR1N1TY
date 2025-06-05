#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#



def queensAttack(n, k, r_q, c_q, obstacles):
    n_squares = {
        "N": n - r_q,
        "NE": min(n - r_q, n - c_q),
        "E": n - c_q,
        "SE": min(r_q - 1, n - c_q),
        "S": r_q - 1,
        "SW": min(r_q - 1, c_q - 1),
        "W": c_q - 1,
        "NW": min(n - r_q, c_q - 1)
    }
    for element in obstacles:
        direction = ""
        r_o, c_o = element[0], element[1]
        if c_o == c_q:
            if r_o > r_q:
                direction = "N"
            if r_o < r_q:
                direction = "S"
        elif r_o == r_q:
            if c_o > c_q: 
                direction = "E"
            if c_o < c_q:
                direction = "W"
        elif abs(r_o - r_q) == abs(c_o - c_q):
            if r_o > r_q and c_o > c_q:
                direction = "NE"
            if r_o > r_q and c_o < c_q:
                direction = "NW"
            if r_o < r_q and c_o > c_q:
                direction = "SE"
            if r_o < r_q and c_o < c_q:
                direction = "SW"
        if direction:
            if direction in ("E", "W"):
                distancia = abs(c_o - c_q) - 1
            else:
                distancia = abs(r_o - r_q) - 1
            n_squares[direction] = min(n_squares[direction], distancia)
        if not direction:
            continue     
    return sum(n_squares.values())   
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
