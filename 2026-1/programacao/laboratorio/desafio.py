nome = input("Digite seu nome: ")
print(f"Letras de '{nome}':")
for letra in nome:
    print(f" -> {letra}")

# Contar vogais
vogais = "aeiou"
contagem = 0
for letra in nome:
    if str.lower(letra) in vogais:
        contagem += 1

print(f"'{nome}' tem {contagem} vogal(is).")

