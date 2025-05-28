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

