"""
Exercício 13 - Potência sem Operador
Leia uma base e um expoente (inteiro positivo). Calcule base ** expoente usando apenas multiplicações em um loop, sem usar o operador **.

Exemplo de saída:

Base: 3
Expoente: 4
3 ^ 4 = 81

3 * 3 * 3 * 3
9 * 9
81
"""


try:
    base = int(input("Base: "))    
    expoente = int(input("Expoente: "))

    i = 1
    resultado = 1
    while (i<=expoente):
        resultado = resultado * base
        i=i+1

    print(f"{base} ^ {expoente} = {resultado}")    

except (ValueError):
    print("Erro: Input inválido.")