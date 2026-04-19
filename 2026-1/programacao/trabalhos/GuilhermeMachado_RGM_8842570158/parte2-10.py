"""
Exercício 10 - Somatório Interativo
Leia números do usuário até ele digitar 0. 
Ao final, exiba: - 
1) A soma de todos os números - 
2) A quantidade de números digitados - 
3) A média dos valores
"""

try:
    quantidade = 0
    soma = 0
    numero = int(input("Numero 1: "))        
    while numero!=0:
        quantidade += 1        
        soma = soma + numero        
        numero = int(input("Numero 1: "))            
    
    print(f"Soma de todos os números: {soma}")    
    print(f"Quantidade de números digitados: {quantidade}")    
    print(f"Média dos valores: {soma/quantidade}")    

except (ValueError):
    print("Erro: Input inválido.")