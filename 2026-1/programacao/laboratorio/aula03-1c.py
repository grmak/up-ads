"""
Leia a nota (0-10) e o nº de faltas de um aluno
(máx 30 aulas).
Exiba True/False para:
• aprovado_nota: nota >= 7
• freq_ok: faltas <= 9 (máx 25% de 30)
• aprovado: ambas as condições
"""

nota = int(input("Nota: "))
faltas = int(input("Faltas: "))

aprovado_nota = (nota >= 7) 
aprovado_freq = (faltas <= 9)

if aprovado_nota and aprovado_freq:
    print('Aprovado') 
else:
    print('Reprovado') 
   
