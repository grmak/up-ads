"""
Exercício 15 - Validação de Nota
Leia uma nota do usuário. Se a nota for inválida (menor que 0 ou maior que 10), 
peça novamente até o usuário digitar um valor válido. Ao final, exiba a nota aceita.
"""


try:
    nota = -1
    while not (nota in range(0, 11)):
        nota = int(input("Nota: "))    
    
    print()
    print(f"Nota aceita: {nota}")    

except (ValueError):
    print("Erro: valor inválido")