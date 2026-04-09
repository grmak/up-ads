"""
Desafio — Cheque Digital
O último dígito de um número pode ser obtido com %

Leia um número inteiro n e exiba:
• Seu último dígito (n % 10)
• Se n é par (True/False) (n % 2 == 0)
• Se n é divisível por 3 e por 5 ao mesmo tempo
"""

numero = int(input("Número: "))
ultimo = numero % 10
numero_par = (numero % 2) == 0
numero_divisivel = (numero % 3 == 0) and (numero % 5 == 0)

print("Último nr: ", ultimo)
print("Numero par: ", numero_par)
print("Divisivel por 3 e 5: ", numero_divisivel)



