from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Ej. A:3, B:3, C:1 - n=3
        freq = Counter(tasks)                
        max_freq = max(freq.values())  
        #Indica el número de bloques A---A---A   
        max_count = list(freq.values()).count(max_freq)  
        # Indica el tamaño extra del último bloque AB--AB--AB
        part_count = max_freq - 1            
        # Número de bloques completos (2) AB--
        part_length = n + 1             
        #Longitud de cada bloque = 4
        empty_slots = part_count * part_length + max_count  
        #Cálculo del tamaño de cada bloque + extra
        return max(len(tasks), empty_slots)  
        #Retornar si tasks puede cubrir espacios en su totalidad
