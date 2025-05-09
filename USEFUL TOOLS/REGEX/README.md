# Módulo re

Evaluación de expresiones regulares. 

## re.match(pattern, string)

Coincidencia de la cadena ingresada con el patrón establecido.

Retornar True/False

```
import re
P = input()
print (bool(re.match(regex, P)))
```

Retornar la primera detección **al principio** de la cadena en específico

```
import re
result = re.match(r"\d+", "123abc")
if result:
    print(result.group())  # "123"
```

## re.search(pattern, string)

Retornar la primera detección **en cualquier parte** de la cadena en específico

```
import re
result = re.search(r"\d+", "abc123")
if result:
    print(result.group())  # "123"
```

## re.findall(pattern, string)

Devuelve todas las cadenas que coinciden con el patrón en forma de lista.

```
import re
result = re.findall(r"\d+", "abc123xyz456def")
print(result)  # ["123", "456"]
```

## re.finditer(pattern, string)

Variación de findall que retorna un iterador con objetos match, que contiene info detallada sobre cada coincidencia.

```
import re

# Cadena de ejemplo
text = "El ID123a es válido, pero el ID456b no lo es. El ID789c es otro ejemplo."

# Expresión regular para buscar números después de "ID"
pattern = r"ID(\d+)(\w)"

# Usar re.finditer para obtener el iterador de coincidencias
matches = re.finditer(pattern, text)

# Iterar sobre las coincidencias
for match in matches:
    # Acceder a la coincidencia completa
    print("Coincidencia completa:", match.group(0))
    
    # Acceder al grupo capturado (número)
    print("Letra después del número:", match.group(2))
    
    # Acceder a la posición (inicio, fin) de la coincidencia
    print("Posición de la coincidencia:", match.span())

    print("-" * 40)
```

Coincidencia completa: ID123a
Número después de 'ID': a
Posición de la coincidencia: (3, 9)
----------------------------------------
Coincidencia completa: ID456b
Número después de 'ID': b
Posición de la coincidencia: (29, 35)
----------------------------------------
Coincidencia completa: ID789c
Número después de 'ID': c
Posición de la coincidencia: (49, 55)
----------------------------------------


## re.sub(pattern, string)

Sustituye todas los patrones con otra cadena.

```
import re
result = re.sub(r"\d+", "number", "abc123xyz456")
print(result)  # "abcnumberxyznumber"
```

## re.subn(pattern, string)

Sustituye todas los patrones con otra cadena y retorna el número de sustituciones realizadas.

```
import re
result = re.subn(r"\d+", "number", "abc123xyz456")
print(result)  # ("abcnumberxyznumber", 2)
```
## re.split(pattern, string)

Divide en la cadena separando en función de todas las coincidencias del patrón.

```
import re
result = re.split(r"\d+", "abc123xyz456def")
print(result)  # ['abc', 'xyz', 'def']
```

## re.fullmatch(pattern, string)

Asegura que toda la cadena coincida con el patrón.

```
import re
result = re.fullmatch(r"\d+", "12345")
if result:
    print(result.group())  # "12345"
```

# Objetos match generados por re

Cuando re.match(), re.search(), re.finditer() o re.fullmatch() encuentran una coincidencia, devuelven un objeto match que proporciona varios métodos útiles para trabajar con las coincidencias.

## match.group()

Devuelve el contenido de los grupos de la coincidencia. Si no se especifican los grupos, devuelve toda la coincidencia.

```
import re
result = re.match(r"(\d+)([a-z]+)", "123abc")
print(result.group(0))  # "123abc"
print(result.group(1))  # "123"
print(result.group(2))  # "abc"
```
## match.start() / match.end()/ match.span()

Devuelve la posición de inicio, final, o tupla de inicio y final, de la coincidencia o del grupo especificado.

```
import re
result = re.search(r"(\d+)([a-z]+)", "abc123xyz")
print(result.start(1))  # Posición de inicio del grupo 1 ("123") -> 3
```


# REGEX



# Conjunto de Caracteres Simples

\[a-z] -> Letras de la 'a' a la 'z'

\[A-Z] -> Letras de la 'A' a la 'Z'

\[0-9] -> Números del 0 al 9


## Metacaracteres
'^' -> Inicio de línea

'\' -> Ingresa el siguiente caracter literal (Para caracteres conflictivos)

'|' -> Caracter or

'.' -> Cualquier tipo de caracter

'\d' -> Números enteros

'\D' -> No Dígitos

'\w' -> Caracteres de palabra (letras, dígitos, ...)

'\W' -> No Caracteres de palabra

'\s' -> Espacios en blanco, tabulaciones y saltos de línea

'\S' -> No saltos

'$' - > Fin de línea



## Cuantificadores

'*' -> Cero o más veces

'+' -> Uno o más veces

'?' -> Cero o una vez

'{n}' -> Exactamente n veces

'{n,}' -> Al menos n veces

'{n,m}' -> Entre n y m veces

## Estructuras y Captura

'[]' -> Conjunto de caracteres

'\[^...]' -> No pertenece al conjunto (Negación)

'()' -> Agrupación de caracteres (captura)


## Captura (para referirlo después) y Acceso

'()' ->	Agrupación (captura)

'(?:)' -> Agrupación sin captura

'\1' '\2' -> Acceso a capturas realizadas previamente

## Lookahead y Lookbehind

'(?=...)' ->	Lookahead positivo (sigue un patrón)	Ej. \d(?=\D) → un dígito seguido de no-dígito

'(?!...)'	-> Lookahead negativo (no sigue un patrón)	Ej. \d(?!\d) → un dígito no seguido de otro dígito

'(?<=...)' ->	Lookbehind positivo (precede un patrón)	Ej. (?<=@)\w+ → palabras después de '@'

'(?<!...)' ->	Lookbehind negativo (no precede un patrón)	(?<!@)\w+ → palabras no precedidas por '@'

## Metacaracteres menos usados

\b...\b -> La cadena puede aparecer en los límites de la cadena

\B...\B -> La palabra no puede aparecer al inicio o al final de la cadena

\A: Coincide con el inicio de la cadena (similar a ^, pero siempre al principio de toda la cadena, no de cada línea).

\Z: Coincide con el final de la cadena (similar a $, pero siempre al final de toda la cadena, no de cada línea).
