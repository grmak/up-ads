"""
DESAFIO — Fatura de Energia Completa

Leia: nome do titular, consumo em kWh dos últimos 3 meses. 

Defina TARIFA = 0.85 e TAXA_IP = 0.08.
Calcule: consumo médio, valor de cada mês, média, imposto e total geral.
Exiba uma fatura formatada com o mês atual obtido via datetime.now().strftime('%B/%Y'),
todos os valores com R$ e :.2f, e o nome centralizado em 40 chars. Use snake_case e constantes.

DICA
from datetime import datetime | TARIFA = 0.85 | TAXA_IP = 0.08
nome_titular = input('Titular: ')
kwh1 = float(input('kWh mês 1: ')) | kwh2 = ... | kwh3 = ...
valor1 = kwh1 * TARIFA | ... | media = (valor1+valor2+valor3)/3 | imposto = (valor1+valor2+valor3)*TAXA_IP

"""
TARIFA = 0.85
TAXA_IP = 0.08

titular = input("Nome do titular: ") 
kwh1 = float(input("kwh1 mês 1: "))
kwh2 = float(input("kwh1 mês 2: "))
kwh3 = float(input("kwh1 mês 3: "))

media_kwh  = (kwh1+kwh2+kwh3)/3
valor1 = kwh1 * TARIFA
valor2 = kwh2 * TARIFA
valor3 = kwh3 * TARIFA
media  = (valor1+valor2+valor3)/3
imposto = (valor1+valor2+valor3) * TAXA_IP
consumo_medio = (valor1 + valor2 + valor3) / 3


titular = 'GUILHERME'

print("\n" + "="*40)
print(f"{titular:^40}")
print("="*40)

print(f"{'Média de consumo':.<20}{media_kwh:>10.2f} kmh")
print(f"{'Média':.<20}{media:>10.2f}")
print(f"{'Média de consumo':.<20}{media_kwh:>10.2f}")
print(f"{'Imposto':.<20}{imposto:>10.2f}")
print(f"{'Consumo médio':.<20}{consumo_medio:>10.2f}")