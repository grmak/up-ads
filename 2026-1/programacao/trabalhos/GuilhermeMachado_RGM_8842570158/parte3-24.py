"""
Exercício 24 - Calculadora de Média da Turma
Leia as notas de uma turma (quantidade indefinida, use while). O usuário digita -1 para encerrar. Ao final, exiba:

Quantidade de alunos
Maior e menor nota
Média da turma
Quantidade de aprovados (>= 7), recuperação (>= 5 e < 7) e reprovados (< 5)
Percentual de aprovação
"""

APROVADO = 1
RECUPERACAO = 0
REPROVADO = -1

def f_situacao(lnotas, situacao)->int:        
    qtde = 0
    for nota in lnotas:
        if (situacao == -1) and (nota < 5): 
            qtde = qtde+1
        elif (situacao == 1) and (nota >= 7): 
            qtde = qtde+1
        elif (situacao == 0) and (nota >= 5) and (nota < 7): 
            qtde = qtde+1
    return qtde

def f_media(lnotas)->float:
    soma = 0
    for nota in lnotas:
        soma = soma+nota
    return soma/len(lnotas)

def f_menor(lnotas)->int:        
    menor = lnotas[0]
    for nota in lnotas:
        if nota < menor:
            menor = nota    
    return menor

def f_maior(lnotas)->int:        
    maior = lnotas[0]
    for nota in lnotas:
        if nota > maior:
            maior = nota    
    return maior

try:
    quantidade = 0
    soma = 0    
    nota = 0
    notas = []
    qtde_reprovados = qtde_aprovados = qtde_recuperacao = 0
    while nota!=-1:
        nota = int(input("Nota: ")) 
        if nota > 10:
            print('Nota inválida')
            continue
        if nota!=-1:
          notas.append(nota)
    
    print("="*50)
    print(f"Quantidade de alunos: {len(notas)}")
    print(f"Maior nota: {f_maior(notas)}")    
    print(f"Menor nota : {f_menor(notas)}")            
    print(f"Média da turma: {f_media(notas)}")            
    print(f"Qtde aprovados: {f_situacao(notas, APROVADO)}")
    print(f"Qtde recuperação: {f_situacao(notas, RECUPERACAO)}")    
    print(f"Qtde reprovados: {f_situacao(notas, REPROVADO)}")    

except (ValueError):
    print("Erro: input inválido.")