"""
Exercício 22 - Desenho de Triângulo
Leia a altura de um triângulo e desenhe usando *:
Desafio extra: Desenhe também o triângulo centralizado:

     *
    ***
   *****
  *******
 *********
***********
"""

def dobro_menos_1(valor: int) -> int:
  return valor * 2 -1

try:    
    altura = int(input("Altura: "))
    for i in range(0, altura):                            
        asteriscos =  '*' * (dobro_menos_1(i))
        largura = dobro_menos_1(altura) 
        print(f"{asteriscos:^{largura}}")

except (ValueError):
    print("Erro: Input inválido.")