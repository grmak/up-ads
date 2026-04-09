"""
Exercício 2 - Aprovação Escolar
Leia duas notas de um aluno e calcule a média aritmética. Classifique:

Média >= 7.0: Aprovado
Média >= 5.0 e < 7.0: Recuperação
Média < 5.0: Reprovado
Exemplo de saída:

Nota 1: 6.0
Nota 2: 8.0
Média: 7.00 - APROVADO
"""

try:
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    media = (nota1 + nota2) / 2
    
    if (media >= 7.0):        
        print(f"Média: {media} - APROVADO")
    elif (media >= 5.0) and (media < 7.0):
        print(f"Média: {media} - RECUPERAÇÃO")
    elif (media < 5.0):
        print(f"Média: {media} - REPROVADO")

except ValueError:
    print("Erro: você não digitou uma nota válida.")