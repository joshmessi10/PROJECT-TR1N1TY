# Módulo Itertools
Generar diferentes combinaciones y permutaciones de elementos.


## itertools.product()
Combinando todo con todo. Las repeticiones no importan (tupla 2,2), el orden tampoco (1,2 es dif de 2,1).

```
from itertools import product
list(product([1, 2, 3], 2))
#Resultado: [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
```

## itertools.combinations()
Combinando todo con todo, pero tanto las repeticiones como el orden importan (se eliminan las tuplas que tienen los mismos elementos o elementos repetidos).

```
from itertools import combinations
list(combinations([1, 2, 3], 2))
#Resultado: [(1, 2), (1, 3), (2, 3)]
```

## itertools.permutations()
Permutando todo con todo, pero las repeticiones sí importan (se eliminan las tuplas con elementos repetidos).

```
from itertools import permutations
list(permutations([1, 2, 3], 2))
#Resultado: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
```

## itertools.combinations_with_replacement()
Combinando todo con todo, pero el orden sí importa (se eliminan las tuplas que tienen los mismos elementos).

```
from itertools import combinations_with_replacement
print(list(combinations_with_replacement([1, 2, 3], 2)))
#Resultado: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
```

## itertools.accumulate()
Suma acumulada de los valores del arreglo. Similar a frecuencia acumulada en estadística.

```
from itertools import accumulate
list(accumulate([1, 2, 3, 4]))
# [1, 3, 6, 10]
```

## itertools.groupby()
Agrupa elementos consecutivos iguales.

```
from itertools import groupby
[(k, list(g)) for k, g in groupby('AAABBBCCDA')]
# [('A', ['A', 'A', 'A']), ('B', ['B', 'B', 'B']), ('C', ['C', 'C']), ('D', ['D']), ('A', ['A'])]
```

## itertools.starmap()
Aplica una función a los elementos que desempaqueta.

```
from itertools import starmap
list(starmap(pow, [(2, 5), (3, 2)]))
# [32, 9]
```
