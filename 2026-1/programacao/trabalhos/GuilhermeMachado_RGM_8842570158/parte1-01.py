"""
Exercício 1 - Positivo, Negativo ou Zero
Leia um número inteiro e informe se ele é positivo, negativo ou zero.

Exemplo de saída:

Digite um número: -3
O número -3 é negativo.
"""

try:
    numero = int(input("Digite um número inteiro: "))
    if (numero == 0):
        print("Zero")
    elif (numero > 0):
        print(f"O número {numero} é positivo")
    elif (numero < 0):
        print(f"O número {numero} é negativo")

except ValueError:
    print("Erro: Input inválido.")