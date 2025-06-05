# Módulo Itertools
Generar diferentes combinaciones y permutaciones de elementos.


## itertools.product(items, r)
Combinando todo con todo, generando tuplas de tamaño r. Las repeticiones no importan (tupla 2,2), el orden tampoco (1,2 es dif de 2,1).

```
from itertools import product
print(list(product([1,2,3], [2,3])))
#Resultado: [(1, 2), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]
```

## itertools.combinations(items, r)
Combinando todo con todo, generando tuplas de tamaño r, pero tanto las repeticiones como el orden importan (se eliminan las tuplas que tienen los mismos elementos o elementos repetidos).

```
from itertools import combinations
list(combinations([1, 2, 3], 2))
#Resultado: [(1, 2), (1, 3), (2, 3)]
```

## itertools.permutations(items, r)
Permutando todo con todo, generando tuplas de tamaño r, pero las repeticiones sí importan (se eliminan las tuplas con elementos repetidos).

```
from itertools import permutations
list(permutations([1, 2, 3], 2))
#Resultado: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

## itertools.combinations_with_replacement(items, r)
Combinando todo con todo, generando tuplas de tamaño r, pero el orden sí importa (se eliminan las tuplas que tienen los mismos elementos).

```
from itertools import combinations_with_replacement
print(list(combinations_with_replacement([1, 2, 3], 2)))
#Resultado: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

## itertools.accumulate(items, func)
Suma acumulada de los valores del arreglo. Similar a frecuencia acumulada en estadística.

```
from itertools import accumulate
list(accumulate([1, 2, 3, 4]))
# [1, 3, 6, 10]
```

Permite integrar funciones ya conocidas de python, o de operator.

```
from itertools import accumulate

print(list(accumulate([1, 5, 2, 8, 3], max)))  # [1, 5, 5, 8, 8]

print(list(accumulate([9, 7, 8, 2, 5], min)))  # [9, 7, 7, 2, 2]
```

```
from itertools import accumulate
import operator

print(list(accumulate([1, 2, 3, 4], operator.mul)))  # [1, 2, 6, 24]
```

## itertools.groupby(items, key)
Agrupa elementos consecutivos iguales. No están ordenados. (Se pueden ordenar usando el metodo sorted(). )

```
from itertools import groupby
[(k, list(g)) for k, g in groupby('AAABBBCCDA')]
# [('A', ['A', 'A', 'A']), ('B', ['B', 'B', 'B']), ('C', ['C', 'C']), ('D', ['D']), ('A', ['A'])]
```

Se puede utilizar una llave para agrupar en función del resultado de la función lambda en el arreglo. Por ejemplo, agrupar pares e impares:

```
from itertools import groupby

nums = [1, 3, 5, 2, 4, 6, 1, 3]

for k, g in groupby(nums, key=lambda x: x % 2):
    print(k, list(g))

#1 [1, 3, 5]   # impares (x % 2 == 1)
#0 [2, 4, 6]   # pares   (x % 2 == 0)
#1 [1, 3]      # impares otra vez (no consecutivos, se agrupan de nuevo)
```





## itertools.starmap()
Aplica una función a los elementos que desempaqueta.

```
from itertools import starmap
list(starmap(pow, [(2, 5), (3, 2)]))
# [32, 9]
```

## itertools.chain(n_iterables)
Combina diferentes conjuntos de iteradores (tuplas, listas, generadores) en uno solo.

```
import itertools

# A tuple and a list
tuple1 = (10, 20)
list2 = [30, 40]

# Using itertools.chain to combine them
combined = itertools.chain(tuple1, list2)

# Convert to a list and print
print(list(combined)) # Output: [10, 20, 30, 40]
```

```
import itertools

# Two generators
gen1 = (x for x in range(3))  # generator: (0, 1, 2)
gen2 = (x for x in range(3, 6))  # generator: (3, 4, 5)

# Using itertools.chain to combine the generators
combined = itertools.chain(gen1, gen2)

# Convert to a list and print
print(list(combined))  # Output: [0, 1, 2, 3, 4, 5]
```
