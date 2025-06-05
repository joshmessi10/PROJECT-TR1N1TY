# Módulo Collections

Extensión de las funcionalidades de los tipos de datos estándar (como listas, diccionarios, etc.) para hacer el manejo de datos más eficiente y flexible.

# Counter

Conteo de frecuencia de elementos en una colección. Retorna un diccionario con elemento y cantidad.

```
data = ['a', 'b', 'c', 'a', 'b', 'a']
counter = Counter(data)
print(counter)  # Counter({'a': 3, 'b': 2, 'c': 1})
```

## Counter.mostcommon(n)

Retorna los n elementos más repetidos.

```
counter = Counter('abracadabra')
print(counter.most_common(2))  # [('a', 5), ('b', 2)]
```

## Counter.elements()

Iterador que retorna los elementos repetidos según orden de repetición.

```
counter = Counter('abracadabra')
print(list(counter.elements()))  # ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'r', 'r', 'c', 'd']
```

# defaultdict

defaultdict es una subclase de dict que permite asignar un valor por defecto a las claves que no existen en el diccionario. 
```
from collections import defaultdict

# Creando un defaultdict con valores por defecto como una lista vacía
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)  # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})
```

Cuando accedes a una clave que no está presente, en lugar de lanzar un KeyError, devuelve el valor por defecto especificado al crear el defaultdict.
```
d2 = defaultdict(int)
d2['x'] += 1
print(d2)  # defaultdict(<class 'int'>, {'x': 1})
```

Cuando preguntas por una clave inexistente, retorna el valor por defecto al inicializar defaultdict.

```
from collections import defaultdict

d = defaultdict(int)  # Cualquier clave nueva empieza con 0
print(d['no_existe'])  # 0
```

Inicialización personalizada con lambda

```
from collections import defaultdict
d = defaultdict(lambda: 100)

print(d['x'])  # 100
d['x'] += 23
print(d['x'])  # 123
```

# deque

Permite implementar una cola con entrada y salida por ambos extremos.

.append(): Añade un elemento al final.

.appendleft(): Añade un elemento al principio.

.pop(): Elimina el último elemento.

.popleft(): Elimina el primer elemento.

```
from collections import deque

# Crear un deque
dq = deque([1, 2, 3])
print(dq)  # deque([1, 2, 3])

# Añadir elementos a la izquierda y derecha
dq.append(4)    # Añadir a la derecha
dq.appendleft(0)  # Añadir a la izquierda
print(dq)  # deque([0, 1, 2, 3, 4])

# Eliminar elementos de la derecha e izquierda
dq.pop()       # Eliminar de la derecha
dq.popleft()   # Eliminar de la izquierda
print(dq)  # deque([1, 2, 3])
```

# OrderedDict

Diccionario que mantiene el orden, en este caso, en que fueron insertados.

```
from collections import OrderedDict

# Crear un OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)  # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Moviendo un elemento al final
od.move_to_end('a')
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Moviendo un elemento al principio
od.move_to_end('b', last=False)
print(od)  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])
```

# ChainMap

Encadenamiento de diccionarios.

```
from collections import ChainMap

# Crear dos diccionarios
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Crear un ChainMap
chain_map = ChainMap(dict1, dict2)
print(chain_map)  # ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})

# Acceder a los elementos
print(chain_map['a'])  # 1
print(chain_map['b'])  # 2 (se toma de dict1)
print(chain_map['c'])  # 4 (se toma de dict2)
```

# namedtuple

Tuplas con nombre para claridad y eficiencia.

```
from collections import namedtuple

Point = namedtuple('Point', 'x y')
p = Point(1, 2)
print(p.x, p.y)
```
