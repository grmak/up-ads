"""
Contracheque Formatado

Leia nome (str), salário bruto (float) e % de desconto.

Calcule o salário líquido.
Exiba um contracheque com nome alinhado à esquerda em 20 chars, 
salário bruto e líquido com R$ e :.2f, e desconto em %

"""

nome = input("Nome: ")
salario_bruto = float(input("Salário bruto: "))
desconto = int(input("Percentual de desconto : "))
salario_liquido = salario_bruto - (salario_bruto * desconto) / 100

print("\n" + "="*50)
print("CONTRACHEQUE")
print("="*50)
print(f"{nome:.<20} R${salario_bruto:>8.2f}")
print(f"{'Desconto':.<20}{desconto:>5.1f}%")
print(f"{'Salário Líquido':.<20} R${salario_liquido:>8.2f}")

