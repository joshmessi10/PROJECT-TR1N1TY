# 🔍 ¿Qué es la recursión?

La **recursión** es una técnica donde una función se **llama a sí misma** para resolver un problema más pequeño del original, hasta alcanzar un caso base.

En términos simples:

> Divide y vencerás: un problema grande se resuelve resolviendo una versión más pequeña de sí mismo.

---

## 📦 Estructura básica

```python
def funcion():
    if caso_base:
        return resultado
    else:
        return funcion_mas_pequeña()
