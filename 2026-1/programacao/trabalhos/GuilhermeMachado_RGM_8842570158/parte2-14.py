"""
Exercício 14 - Contagem Regressiva Personalizada
Leia um número inicial e um passo. Faça uma contagem regressiva usando while.

Exemplo (início=20, passo=3):

20 17 14 11 8 5 2
Fim da contagem!
"""


try:
    inicio = int(input("Inicio: "))    
    passo = int(input("Passo: "))

    for i in range(inicio, 0, -passo):
        print(f"{i}", end=' ')
    
    print()
    print("\n Fim da contagem")    

except (ValueError):
    print("Erro: Input inválido.")