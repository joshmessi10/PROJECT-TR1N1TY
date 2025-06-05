import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = list(input())
    s.sort()
    c = Counter(s)
    top_three = c.most_common(3)
    for key, value in top_three:
        print(f"{key} {value}")
    
