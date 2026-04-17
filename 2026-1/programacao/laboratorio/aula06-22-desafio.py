"""
Exercício 22 - Desenho de Triângulo
Leia a altura de um triângulo e desenhe usando *:

Triângulo alinhado à esquerda (altura=5):

*
**
***
****
*****
Desafio extra: Desenhe também o triângulo centralizado:

    *
   ***
  *****
 *******
*********
"""

try:    
    altura = int(input("Altura: "))
    for i in range(0, altura):            
        asteriscos =  '*' 
        largura = altura * 2 - 1
        print(f"{asteriscos:^{largura}}")

except (ValueError):
    print("Erro: input inválido")