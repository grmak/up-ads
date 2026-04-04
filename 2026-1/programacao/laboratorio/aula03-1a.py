# Calculadora Básica
# Leia dois números inteiros a e b. Calcule e exiba, um por linha:
# • Soma, diferença, produto
# • a / b e a // b (compare os resultados!)
# • a % b e a ** b

n1 = int(input(f"{'Número 1':.<20}:"))
n2 = int(input(f"{'Número 2':.<20}:"))

soma = n1+n2
subtracao = n1-n2
produto = n1*n2
divsimples = n1/n2
divdupla = n1//n2
resto = n1%n2
potencia = n1**n2

print("")
print(f"{'Soma':.<20}: {soma}")
print(f"{'Subtracao':.<20}: {subtracao}")
print(f"{'Produto':.<20}: {produto}")
print(f"{'Divisão real':.<20}: {divsimples}")
print(f"{'Divisão inteira':.<20}: {divdupla}")
print(f"{'Resto':.<20}: {resto}")
print(f"{'Potencia':.<20}: {potencia}")
