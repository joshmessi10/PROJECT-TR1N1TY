import math
import os
import random
import re
import sys


pattern = r"(?<=\w)[\W#]+(?=\w)"

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = [[0] * n for _ in range(m)]

for i in range(n):
   for j in range(m):
       result[j][i] = matrix[i][j]
       
string = ""
for row in result:
    string += "".join(row)

result = re.sub(pattern, " ", string)
print(result)
