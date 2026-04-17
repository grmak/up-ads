"""
Exercício 24 - Calculadora de Média da Turma
Leia as notas de uma turma (quantidade indefinida, use while). O usuário digita -1 para encerrar. Ao final, exiba:

Quantidade de alunos
Maior e menor nota
Média da turma
Quantidade de aprovados (>= 7), recuperação (>= 5 e < 7) e reprovados (< 5)
Percentual de aprovação
"""

try:
    quantidade = 0
    soma = 0
    numero = int(input("Numero 1: "))        
    while numero!=0:
        quantidade += 1        
        soma = soma + numero        
        numero = int(input("Numero 1: "))            
    
    print(f"Soma de todos os números: {soma}")    
    print(f"Quantidade de números digitados: {quantidade}")    
    print(f"Média dos valores: {soma/quantidade}")    

except (ValueError):
    print("Erro: número inválido.")