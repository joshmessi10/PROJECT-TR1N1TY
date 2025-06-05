class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Agregamos 'L' al inicio y 'R' al final para facilitar el manejo de bordes
        dominoes = 'L' + dominoes + 'R'
        result = []
        i = 0  # puntero al primer dominó importante (L o R)

        # Recorremos desde el segundo caracter
        for j in range(1, len(dominoes)):
            if dominoes[j] == '.':
                continue
            middle = j - i - 1  # cuántos puntos hay entre i y j
            if i > 0:
                result.append(dominoes[i])  # agregamos el dominó de inicio del segmento
            # Caso 1: 'L...L' → todo cae a la izquierda
            if dominoes[i] == 'L' and dominoes[j] == 'L':
                result.append('L' * middle)
            # Caso 2: 'R...R' → todo cae a la derecha
            elif dominoes[i] == 'R' and dominoes[j] == 'R':
                result.append('R' * middle)
            # Caso 3: 'L...R' → nadie empuja → se quedan parados
            elif dominoes[i] == 'L' and dominoes[j] == 'R':
                result.append('.' * middle)
            # Caso 4: 'R...L' → choque
            else:
                half = middle // 2
                result.append('R' * half)
                if middle % 2 == 1:
                    result.append('.')
                result.append('L' * half)
            i = j  # avanzamos el puntero izquierdo

        return ''.join(result)
