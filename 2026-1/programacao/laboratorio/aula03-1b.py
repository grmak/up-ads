"""
Divisão com Resto

Uma turma tem 35 alunos que serão divididos em grupos de 4.

Calcule: 
1)quantos grupos completos são formados?
2) quantos alunos ficam sem grupo?

Use // e % para resolver.
"""

nr_alunos = int(35)
nr_grupos = int(4)

total_grupos = nr_alunos // nr_grupos
alunos_sem_grupo =  nr_alunos % nr_grupos

print("")
print(f"{'Total de grupos':.<20}: {total_grupos}")
print(f"{'Alunos sem grupo':.<20}: {alunos_sem_grupo}")

