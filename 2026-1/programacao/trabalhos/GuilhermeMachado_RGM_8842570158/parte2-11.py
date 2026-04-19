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
largura = 5
print(f"{'':>11}", end='')
for i in range(1, 11):
    print(f"{i:>{largura}}", end='')
print()

for i in range(1, 11):    
    print(f"Tabuada {i:>2}:", end='')   
    for j in range(1,11):
        print(f"{i*j:>{largura}}", end='')   
    print()       

