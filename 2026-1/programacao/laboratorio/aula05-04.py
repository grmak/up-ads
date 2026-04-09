"""
Exercício 4 - Maior de Três
Leia três valores numéricos e mostre qual é o maior deles. Considere que os valores podem ser iguais.

Exemplo de saída:

Valor 1: 15
Valor 2: 42
Valor 3: 28
O maior valor é: 42
"""

try:
    numero1 = int(input("Valor 1: "))
    numero2 = int(input("Valor 2: "))
    numero3 = int(input("Valor 3: "))
    maior = 0

    if ((numero1 == numero2) and (numero1 == numero3)):
        maior = numero1
    elif ((numero1 > numero2) and (numero1 > numero3)):
        maior = numero1
    elif ((numero2 > numero1) and (numero2 > numero3)):
        maior = numero2
    else:
        maior = numero3
         
    print(f"O maior valor é: {maior}")                

except ValueError:
    print("Erro: você não digitou uma nota válida.")