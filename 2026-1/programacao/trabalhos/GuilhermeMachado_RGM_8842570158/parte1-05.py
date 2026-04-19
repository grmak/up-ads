"""
Exercício 5 - Classificador de Triângulos
Leia três lados de um triângulo e determine:

Primeiro, verifique se os valores formam um triângulo válido (cada lado deve ser menor que a soma dos outros dois).
Se for válido, classifique como:
Equilátero (3 lados iguais)
Isósceles (2 lados iguais)
Escaleno (3 lados diferentes)
"""

try:
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))

    if (lado1<lado2+lado3) and (lado2<lado1+lado3) and (lado3<lado1+lado2):
        if ((lado1 == lado2) and (lado1  == lado3)):
            print(f"Equilátero (3 lados iguais)")
        elif ((lado1 != lado2) and (lado1 != lado3) and (lado2 != lado3)):
            print(f"Escaleno (3 lados diferentes)")
        else:
            print(f"Isósceles (2 lados iguais)")
    else:
        print(f"Não formam um triângulo")

except ValueError:
    print("Erro: Input inválido.")