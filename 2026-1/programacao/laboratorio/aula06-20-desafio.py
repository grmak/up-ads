
"""
Exercício 20 - Caixa Registradora
Simule um caixa de supermercado:

Leia o nome e o preço de cada produto (use while True)
Para encerrar, o usuário digita "fim" no nome do produto
Rejeite preços negativos ou zero (use continue)
Ao final, exiba:
Quantidade de itens
Valor total
Valor médio por item
Se o total for acima de R$ 200, aplique 5% de desconto
"""


try:
    qtde = vlr_total = vlr_medio = 0
    while True:
        produto = str(input("Produto: "))
        if produto == "fim":
            break
        valor = float(input("Preço: "))
        if valor <= 0:
            continue

        qtde += 1
        vlr_total += valor

    vlr_medio = vlr_total / qtde        

    if  vlr_total > 200:
        vlr_total = vlr_total * 0.95

    print(f"Quantidade de itens: {qtde}")
    print(f"Valor total: {vlr_total}")
    print(f"Valor médio por item: {vlr_medio}")
    print(f"Valor total: : {vlr_total:.2f}")    
except (ValueError):
    print("Erro: valor inválido de input")