"""
Exercício 11 - Tabuada Completa
Gere a tabuada do 1 ao 10 usando loops aninhados. 
Formate a saída como uma tabela.

Exemplo de saída (parcial):

     1   2   3   4   5   6   7   8   9  10
 1:  1   2   3   4   5   6   7   8   9  10
 2:  2   4   6   8  10  12  14  16  18  20
...
"""

""" Cabeçalho"""
for i in range(1, 11):
    print(f"   {i} ", end='')

print("")
tabuada=""
for i in range(1, 11):    
    for j in range(1,11):
        tabuada = (f"{i*j}")
    print(f"{i}:", end='')

