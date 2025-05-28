# 🔍 ¿Qué es la recursión?

La **recursión** es una técnica donde una función se **llama a sí misma** para resolver un problema más pequeño del original, hasta alcanzar un caso base.

En términos simples:

> Divide y vencerás: un problema grande se resuelve resolviendo una versión más pequeña de sí mismo.

---

## 📦 Estructura básica

```
def funcion():
    if caso_base:
        return resultado
    else:
        return funcion_mas_pequeña()
```

## Ejemplo Clásico: Factorial

```
def factorial(n):
    if n == 0 or n == 1:
        return 1  # caso base
    return n * factorial(n - 1)  # llamada recursiva
```

## ¿Cuándo usar recursión en competencias?

La recursión te permite:

Resolver problemas de combinatoria y conteo

Explorar todas las posibles decisiones (backtracking)

Implementar algoritmos como:

- Árboles binarios
- Búsqueda DFS / BFS
- Algoritmos de división y conquista (merge sort, quick sort)
- Problemas tipo “suma de subconjuntos”, “cambio de monedas”, “permutaciones”, etc.

## ⚠️ Casos base: El alma de la recursión

Cada función recursiva debe tener uno o más casos base.

Estos son los estados en los que no se hace más llamadas recursivas, y evitan bucles infinitos.

```
def cuenta_regresiva(n):
    if n == 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)
```

## 🐢 Problemas de eficiencia

La recursión simple puede ser muy lenta si repite cálculos. Ejemplo: Fibonacci clásico.

```
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

Complejidad: exponencial (O(2^n))


✅ Solución: Memoización
```
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

Complejidad: O(n)

# ¿Qué es Backtracking?

**Backtracking** es una técnica de programación que explora todas las posibles soluciones de un problema **paso a paso**, **descartando rápidamente aquellas que no cumplen con los requisitos**.

> **Idea clave:** Construye soluciones parciales e “intenta y retrocede” cuando una opción no lleva a una solución válida.


## 🔧 Estructura general

```
def backtrack(opciones, estado_actual):
    if estado_actual es solución:
        guardar solución
        return
    for opción in opciones:
        hacer elección
        backtrack(nuevas opciones, nuevo estado)
        deshacer elección  # volver atrás
```

## Ejemplos Clásicos

### Subconjuntos

```
def subsets(nums):
    result = []
    def backtrack(index, path):
        result.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # retroceder
    backtrack(0, [])
    return result
```

### N-Reinas

```
def solveNQueens(n):
    res = []
    board = [["."] * n for _ in range(n)]
    
    def is_valid(row, col):
        for i in range(row):
            if board[i][col] == "Q":
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == "Q":
                return False
            if col + (row - i) < n and board[i][col + (row - i)] == "Q":
                return False
        return True

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."  # deshacer

    backtrack(0)
    return res
```
