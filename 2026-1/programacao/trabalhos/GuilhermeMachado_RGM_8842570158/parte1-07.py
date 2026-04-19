"""
Exercício 7 - Sistema de Notas com Frequência
Leia a nota final e a frequência (%) de um aluno. Determine:

APROVADO: nota >= 7.0 e frequência >= 75%
REPROVADO por nota: nota < 7.0 e frequência >= 75%
REPROVADO por falta: nota >= 7.0 e frequência < 75%
REPROVADO por nota e falta: nota < 7.0 e frequência < 75%
"""

try:
    nota = float(input("Nota final: "))
    frequencia = int(input("Frequencia : "))    
    
    if (nota >= 7.0) and (frequencia>=75):
        print(f"APROVADO")
    elif (nota < 7.0) and (frequencia>=75):
        print(f"REPROVADO por nota")
    elif (nota >= 7.0) and (frequencia<75):
        print(f"REPROVADO por falta")
    else:
        print(f"REPROVADO por nota e falta")

except ValueError:
    print("Erro: Input inválido.")