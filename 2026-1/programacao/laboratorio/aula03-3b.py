"""
Tabela de Potências

Leia uma base numérica (ex: 2).

Exiba uma tabela formatada com os expoentes de
0 a 10:
Base | Exp | Resultado
2 | 0 | 1
2 | 1 | 2 ... etc (alinhe a direita!)

"""

base = int(input("Base numérica: "))

exp=0
print(f"{'Base':>6} | {'Exp':>3} | {'Resultado':>10}")
while exp <= 10:
    resultado = base ** exp
    print(f"{base:>6.0f} | {exp:>3} | {resultado:>10.0f}")
    exp=exp+1

