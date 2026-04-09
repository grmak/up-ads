"""
Desafio — Dados e Estatística

Simule o lançamento de 2 dados (6 faces) com random.randint.

Exiba os valores de cada dado, a soma e:
    • Se é 'par de dados' (ambos iguais)
    • Se a soma é 7 (mais comum no jogo Ludo!)
"""

import random

lancamento1 = random.randint(1,6)
lancamento2 = random.randint(1,6)

if lancamento1 == lancamento2:
  resultado = 2* (lancamento1 + lancamento2) 
else:
  resultado = (lancamento1 + lancamento2)

print("Lançamento 1: " + str(lancamento1))
print("Lançamento 2: " + str(lancamento2))
print("Casas Ludo  : " + str(resultado))


