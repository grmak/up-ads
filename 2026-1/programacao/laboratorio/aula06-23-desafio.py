"""
Exercício 23 - Análise de Senha
Leia uma senha digitada pelo usuário e analise:

Tem pelo menos 8 caracteres?
Contém pelo menos uma letra maiúscula?
Contém pelo menos um número?
<<<<<<< HEAD
Percorra a string com for e use condicionais para verificar cada critério. 
Ao final, diga se a senha é forte (todos os critérios) 
ou fraca (faltou algum).
"""
=======
Percorra a string com for e use condicionais para verificar cada critério. Ao final, diga se a senha é 
forte (todos os critérios) ou fraca (faltou algum).
"""

senha = input("Digite a senha: ")

if len(senha) >= 8:
    print("A senha tem pelo menos 8 caracteres")
else:
    print("A senha não tem pelo menos 8 caracteres")

if any(char.isupper() for char in senha):
    print("A senha contém pelo menos uma letra maiúscula")
else:
    print("A senha não contém pelo menos uma letra maiúscula")

if any(char.isdigit() for char in senha):
    print("A senha contém pelo menos um número")
else:
    print("A senha não contém pelo menos um número")

if len(senha) >= 8 and any(char.isupper() for char in senha) and any(char.isdigit() for char in senha):
    print("A senha é forte")
else:
    print("A senha é fraca")

>>>>>>> f939322eb82d2ce3356c8516d81826cdefee78e8
