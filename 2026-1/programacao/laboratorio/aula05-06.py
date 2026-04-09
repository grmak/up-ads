"""
Exercício 6 - Calculadora de Desconto
Uma loja oferece desconto baseado no valor da compra:

Valor da compra	Desconto
Até R$ 100,00	Sem desconto
De R$ 100,01 a R$ 500,00	10%
Acima de R$ 500,00	20%

Leia o valor da compra e exiba: o valor original, 
o percentual de desconto, 
o valor do desconto 
e o valor final.
"""

try:
    valor = float(input("Valor 1: "))
    desconto = 0.0
    
    if (valor >= 100.01 and valor <= 500.0):        
        desconto = 10
    elif (valor > 500):
        desconto = 20
    
    valor_desconto = (valor * desconto) / 100
    valor_final = valor - valor_desconto

    print(f"Valor original: {valor}")    
    print(f"Percentual de desconto: {desconto}")    
    print(f"Valor do desconto: {valor_desconto}")    
    print(f"Valor final: {valor_final}")    

except ValueError:
    print("Erro: você não digitou uma nota válida.")