"""
Leia o raio de um círculo. 

Calcule e exiba:
• Área (math.pi * r² — use math.pow ou **)
• Circunferência (2 * math.pi * r)
• Diagonal do quadrado circunscrito (2 * r)

Formate todos com 4 casas decimais.
"""

import math

raio = int(input("Informe o raio:"))
area = math.pow(raio,2)
cincunferencia = math.pi * raio * 2
diagonal = 2 * raio

print("")

print(f"{'Área':.<20}: {area:.4f}")
print(f"{'Cincunferência':.<20}: {cincunferencia:.4f}")
print(f"{'Diagonal':.<20}: {diagonal:.4f}")

