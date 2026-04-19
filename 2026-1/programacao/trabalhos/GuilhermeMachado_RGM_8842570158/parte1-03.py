"""
Exercício 3 - Faixa Etária
Leia a idade de uma pessoa e classifique:

Faixa       Classificação
0 a 11      Criança
12 a 17     Adolescente
18 a 59     Adulto
60 ou mais  Idoso
"""

try:
    idade = int(input("Digite sua idade: "))
    if (idade in range(0,12)):
        print(f"Idade {idade} - Criança")
    elif (idade in range(12,18)):
        print(f"Idade {idade} - Adolescente")
    elif (idade in range(18,60)):
        print(f"Idade {idade} - Adulto")
    elif (idade >= 60):
        print(f"Idade {idade} - Idoso")    
    else:
        print(f"Idade {idade} - Classificação desconhecida")    

except ValueError:
    print("Erro: Input inválido.")