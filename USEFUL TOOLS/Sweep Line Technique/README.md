# Técnica Sweep Line (Línea de Barrido)

La técnica **Sweep Line** es un patrón algorítmico poderoso utilizado para resolver problemas que involucran eventos que ocurren a lo largo de una dimensión (normalmente en una línea o eje). Es muy común en problemas de geometría computacional, programación competitiva y análisis de intervalos.

---

## ¿Qué es la técnica Sweep Line?

Imagina que tienes una línea vertical (la "línea de barrido") que se mueve de izquierda a derecha (o de abajo hacia arriba) sobre un conjunto de puntos, segmentos, intervalos o eventos.

A medida que la línea se desplaza, procesa eventos que ocurren en puntos específicos. Estos eventos pueden ser:

- El inicio de un intervalo.
- El final de un intervalo.
- La aparición de un punto o ciudad.
- Cambios en el estado del sistema (por ejemplo, nubes cubriendo ciudades).

La idea es mantener un estado **actualizado dinámicamente** mientras se avanza, para responder preguntas sobre el problema en tiempo eficiente.

---

## ¿Cuándo usar Sweep Line?

- Cuando tienes múltiples intervalos o segmentos que se solapan.
- Cuando necesitas responder consultas en orden creciente de una coordenada (por ejemplo, tiempo o posición).
- Cuando quieres detectar intersecciones o cubrir regiones.
- Para problemas de intervalos, cobertura, conteo de solapamientos, etc.

---

## ¿Cómo funciona?

1. **Convertir el problema en eventos ordenados**  
   Transformamos la información en eventos con una coordenada clave (por ejemplo, posición `x`) y un tipo de evento (inicio, fin, punto).

2. **Ordenar los eventos**  
   Se ordenan todos los eventos por su coordenada principal. En caso de empate, se define un orden para procesarlos correctamente (por ejemplo, fin antes que inicio).

3. **Mantener una estructura de datos para el estado activo**  
   Mientras la línea se mueve, mantenemos qué elementos están activos (por ejemplo, qué intervalos están abiertos).

4. **Procesar cada evento en orden**  
   Actualizamos el estado activo según el tipo de evento (añadiendo o eliminando intervalos) y calculamos la respuesta deseada.

---

## Ejemplo básico

Supongamos que tienes un conjunto de intervalos en la recta y quieres saber en qué puntos cuántos intervalos se solapan.

- Definimos eventos:  
  - `(inicio del intervalo, +1)`  
  - `(fin del intervalo + 1, -1)`

- Ordenamos eventos por posición.

- Recorremos los eventos, manteniendo un contador de intervalos activos.

- En cada evento, sumamos o restamos según el tipo y sabemos cuántos intervalos cubren ese punto.

---

## Ventajas

- **Eficiencia**: reduce problemas complejos a O(N log N) en la mayoría de casos, debido a la ordenación.
- **Simplicidad conceptual**: convierte problemas dinámicos en una sucesión ordenada de eventos.
- **Generalidad**: aplicable a muchos tipos de problemas, no solo geométricos.

---
