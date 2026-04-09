"""
Relógio de Aniversário

Leia o ano de nascimento do usuário.
Use datetime.now().year para obter o ano atual.

Calcule e exiba:
• Idade aproximada
• Se é maior de idade (True/False com operador
relacional
"""

from datetime import datetime

ano_nascimento = int(input("Ano de aniversário: "))
idade_aproximada = datetime.now().year - ano_nascimento
maioridade = (idade_aproximada > 18)

print('Idade aproximada: ', idade_aproximada)
if maioridade:
  print('<Maior de idade>')
else:
  print('<Menor de idade>')