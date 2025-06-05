# 🐍 Diccionarios en Python

## 🤔 ¿Qué es un diccionario?

Un **diccionario** (`dict`) es una colección **mutable**, **ordenada** (desde Python 3.7) e **indexada por claves inmutables**.

```
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "pais": "Colombia"
}
```

### Crear un diccionario

```
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)  # alternativa con claves string

```

## 🛠️ Funcionalidades clave

### Acceder a valores

```
print(d["a"])        # 1
print(d.get("x"))     # None
print(d.get("x", 0))  # 0 por defecto si no existe
```

### Modificar o agregar elementos

```
d["b"] = 20      # modifica valor de "b"
d["c"] = 3       # agrega nueva clave "c"
```

### Eliminar elementos

```
d.pop("a")        # elimina y devuelve valor de "a"
del d["b"]        # elimina clave 'b'
d.clear()         # elimina todo el contenido
```

### Recorrer un diccionario

```
for clave in d:
    print(clave, d[clave])

for clave, valor in d.items():
    print(clave, valor)
```

### Obtener claves, valores y pares

```
d.keys()      # dict_keys([...])
d.values()    # dict_values([...])
d.items()     # dict_items([...])
```

### Métodos útiles

```
d.update({"x": 10, "y": 20})  # actualiza varios
d.setdefault("z", 0)          # agrega solo si la clave no existe
```

### Diccionario por comprensión

```
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## 🔬 Ejemplo práctico: contar caracteres

```
texto = "banana"
conteo = {}
for letra in texto:
    conteo[letra] = conteo.get(letra, 0) + 1
# {'b': 1, 'a': 3, 'n': 2}
```

# ⚔️ Diccionarios (`dict`) en Competencias de Programación

---

## 🔢 1. Contar frecuencias

```
from collections import Counter

palabra = "banana"
frecuencias = Counter(palabra)
print(frecuencias)  
# {'b': 1, 'a': 3, 'n': 2}
```

## 🔍 2. Buscar si existe un complemento (Two Sum)

```
nums = [2, 7, 11, 15]
target = 9
visto = {}

for i, num in enumerate(nums):
    complemento = target - num
    if complemento in visto:
        print((visto[complemento], i))
        # (0, 1) → nums[0] + nums[1] = 2 + 7 = 9
        break
    visto[num] = i
```

## 💡 3. Memoization con Programación Dinámica

```
memo = {}

def fib(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

print(fib(6))  # 8
```

## 🧠 4. Mapear elementos personalizados

```
letras = "abc"
mapeo = {c: i for i, c in enumerate(letras)}
print(mapeo)
# {'a': 0, 'b': 1, 'c': 2}
```

## 🪄 5. Agrupar por anagramas

```
from collections import defaultdict

palabras = ["eat", "tea", "tan", "ate", "nat", "bat"]
grupos = defaultdict(list)

for palabra in palabras:
    clave = "".join(sorted(palabra))
    grupos[clave].append(palabra)

print(list(grupos.values()))
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

## 📦 6. Representar grafos

```
grafo = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": ["A"]
}
print(grafo["B"])
# ['D']

```

## 🔁 7. Contar ocurrencias en una sola pasada

```
nums = [1, 2, 2, 3, 1, 4]
conteo = {}

for num in nums:
    conteo[num] = conteo.get(num, 0) + 1

print(conteo)
# {1: 2, 2: 2, 3: 1, 4: 1}

```
