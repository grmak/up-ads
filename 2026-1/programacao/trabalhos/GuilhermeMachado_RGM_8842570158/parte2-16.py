"""
Exercício 16 - Sequência de Fibonacci
Leia um valor n e imprima os n primeiros termos da sequência de Fibonacci.

Exemplo (n=8):

0 1 1 2 3 5 8 13

0 1 = 1
1 1 = 2
1 2 = 3
2 3 = 5
3 5 = 8
5 8 = 13
"""

try:
    n = int(input("N primeiros temos da sequencia de Fibonacci: "))
    n_anterior = 0
    n_atual = 1
    print(f"{n_anterior} {n_atual}", end = ' ')        
    for i in range(2, n):        
        soma = n_anterior+n_atual
        n_anterior = n_atual
        n_atual = soma
        print(f"{soma}", end = ' ')        

except (ValueError):
    print("Erro: Input inválido.")