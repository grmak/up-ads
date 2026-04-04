"""
Sorteio de Senha

Gere uma 'senha numérica' de 4 dígitos:
• Use random.randint(0, 9) quatro vezes
• Concatene os dígitos em uma string
• Exiba: 'Senha gerada: XXXX'

Bônus: exiba também a soma dos dígitos.
"""

import random

senha = ""

i = 1
while i <= 4:
    i=i+1
    senha = senha + str(random.randint(0,9))
  

print("Senha gerada: " + senha)
