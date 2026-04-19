"""
Exercício 8 - Calculadora Simples
Leia dois números e um operador (+, -, *, /). Realize a operação correspondente e exiba o resultado. Trate o caso de divisão por zero.

Exemplo de saída:

Primeiro número: 10
Operador: /
Segundo número: 3
10 / 3 = 3.33
"""

try:
    numero1 = int(input("Primeiro número: "))    
    operador = input("Operador: ")
    numero2 = int(input("Segundo número: "))
    resultado = 0

    match operador:
        case "+":
            resultado = numero1+numero2
        case "-":
            resultado = numero1-numero2
        case "/":
            resultado = numero1/numero2
        case "*":
            resultado = numero1*numero2
    
    print(f"{numero1} {operador} {numero2} = {resultado}")             
except ValueError:
    print("Erro: Input inválido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero.")
    