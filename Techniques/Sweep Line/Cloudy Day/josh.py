#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'maximumPeople' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY p
#  2. LONG_INTEGER_ARRAY x
#  3. LONG_INTEGER_ARRAY y
#  4. LONG_INTEGER_ARRAY r
#


def maximumPeople(p, x, y, r):
    populations = {}
    sweep_line = []

    # Agregar eventos de ciudades
    for i in range(len(x)):
        sweep_line.append((x[i], ("city", i)))
        populations[i] = p[i]

    # Agregar eventos de nubes
    for i in range(len(y)):
        sweep_line.append((y[i] - r[i], ("cloud_start", i)))
        sweep_line.append((y[i] + r[i] + 1, ("cloud_end", i)))

    # Orden correcto de eventos en posiciones iguales
    def event_priority(event_type):
        if event_type == "cloud_end": return 0
        if event_type == "city": return 1
        if event_type == "cloud_start": return 2

    sweep_line.sort(key=lambda e: (e[0], event_priority(e[1][0])))

    active_clouds = set()
    base_population = 0
    cloud_gain = defaultdict(int)

    for pos, event in sweep_line:
        etype, eid = event
        if etype == "cloud_start":
            active_clouds.add(eid)
        elif etype == "cloud_end":
            active_clouds.discard(eid)
        elif etype == "city":
            if len(active_clouds) == 0:
                base_population += populations[eid]
            elif len(active_clouds) == 1:
                cloud_id = next(iter(active_clouds))
                cloud_gain[cloud_id] += populations[eid]

    return base_population + max(cloud_gain.values(), default=0)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
