"""
Exercício 12 - Retângulo de Asteriscos
Leia dois valores n (linhas) e m (colunas) e desenhe um retângulo de *.

Exemplo (n=3, m=5):

*****
*****
*****
"""


try:
    m = int(input("Linhas: "))    
    n = int(input("Colunas: "))
    i = 0
    while (i<m):
        print(f"{'*'*n}")
        i+=1

except (ValueError):
    print("Erro: valor inválido")