"""
Exercício 9 - Números Pares
Imprima todos os números pares de 1 a 30 usando for.

Saída esperada:

2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
"""

for i in range(1, 31):
    if (i % 2) == 0:
        print(i, end=" ")      

