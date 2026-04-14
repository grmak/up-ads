"""
Exercício 17 - Verificador de Primos
Leia um número inteiro positivo e informe se ele é primo ou não. 
Se não for primo, mostre por qual número ele é divisível.
"""

try:
    n = int(input("Número: "))
    divisivel=[]

    for i in range(1, n+1):
        if (n%i)==0:
            divisivel.append(i)
    
    if (len(divisivel)==2):
        print(f"O número {n} é primo")
    else:
        print(f"O número {n} não é primo \nÉ divisível por {divisivel}")

except (ValueError):
    print("Erro: valor inválido")