"""
Exercício 15 - Validação de Nota
Leia uma nota do usuário. Se a nota for inválida (menor que 0 ou maior que 10), 
peça novamente até o usuário digitar um valor válido. Ao final, exiba a nota aceita.
"""


try:
    nota_invalida = True
    while nota_invalida:
        nota = int(input("Nota: "))    
        nota_invalida = (nota < 0) or (nota>10)
        if nota_invalida:
            print("Nota inválida, digite outra nota")
    
    print()
    print(f"Nota aceita: {nota}")    

except (ValueError):
    print("Erro: Input inválido.")