"""
Exercício 18 - Maior e Menor de N números
Leia n números (onde n é informado pelo usuário) e, ao final, mostre o maior, o menor e a média de todos os valores.
"""


try:
    n = int(input("Quantidade: "))
    maior = menor = soma = 0
    for i in range(0, n):
        n = int(input("Numero: "))
        soma += n
        if i==0:
            maior = menor = n
        if n < menor:
            menor=n
        if n > maior:
            maior=n       

    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Quantidade: {n}")
    print(f"Soma: {soma}")
    print(f"Média : {soma/n}")
except (ValueError):
    print("Erro: valor inválido")