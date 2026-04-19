
"""
Exercício 21 - Sistema de Pedidos de Lanchonete
Desenvolva um sistema com o cardápio abaixo:

Item	Preço	Disponível
Hambúrguer	R$ 25.00	Sim
Pizza	R$ 35.00	Sim
Suco	R$ 8.00	Não
Batata Frita	R$ 15.00	Sim
Sorvete	R$ 12.00	Não
O sistema deve: - Mostrar o cardápio e permitir pedidos - Ignorar itens em falta (com mensagem de aviso) - 
Limitar a 5 itens por pedido - Permitir cancelar digitando "cancelar" -
Ao final, exibir: lista de itens pedidos, quantidade e valor total
"""

produtos = [
    {"codigo":1, "nome": "Hambúrguer", "preco": 25.00, "disponivel": True},
    {"codigo":2, "nome": "Pizza", "preco": 35.00, "disponivel": True},
    {"codigo":3, "nome": "Suco", "preco": 8.00, "disponivel": False},
    {"codigo":4, "nome": "Batata Frita", "preco": 15.00, "disponivel": True},
    {"codigo":5, "nome": "Sorvete", "preco": 12.00, "disponivel": False}
]

pedido = []

def cardapio(lprodutos):
    print("="*60)
    print(f"{'CARDÁPIO':^60}")
    print("="*60)
    for produto in lprodutos:
        print(f"Código {produto["codigo"]}: {produto["nome"]} | Preço: {produto["preco"]} | Disponível: {produto["disponivel"]}")
    print("="*60)
    print(f"'Cancelar' para encerrar")
    print("="*60)

def qtde_itens(lpedido) -> int:    
    qtde = 0       
    for i in range(0, len(lpedido)):
        produto, quantidade = pedido[i]
        qtde = qtde + quantidade

    return qtde

def fatura(lpedido):
    print("="*60)
    print(f"{'PEDIDO':^60}")
    print("="*60)
    valor_pedido=0.0
    for i in range(0, len(lpedido)):
        produto, quantidade = pedido[i]
        valor_produto = (quantidade * produto["preco"])
        valor_pedido = valor_pedido + valor_produto
        print(f"{quantidade}x{produto["nome"]}: R${valor_produto}")
        
    print("="*60)
    print(f"TOTAL: R${valor_pedido}")    
    print("="*60)

# Mostra o cardápio
cardapio(produtos)

quantidade = 0
escolha = ''
while escolha!='cancelar':    
    escolha = input("Código: ")    
    if escolha=='cancelar':
        break

    codigo = int(escolha)        
    
    if (codigo < 0) or (codigo > len(produtos)):
        print('Código inválido')       
        continue

    produto = produtos[codigo-1]
    if (produto["disponivel"] == False):
        print('Produto indisponível')        
        continue

    quantidade = int(input("Quantidade: "))
    if (qtde_itens(pedido) + quantidade) > 5:
        print('Não é possível solicitar mais que 5 itens')       
        continue    
    
    pedido.append((produtos[codigo-1], quantidade))

fatura(pedido)