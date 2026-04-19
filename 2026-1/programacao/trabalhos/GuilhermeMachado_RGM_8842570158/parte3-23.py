"""
Exercício 23 - Análise de Senha
Leia uma senha digitada pelo usuário e analise:

Tem pelo menos 8 caracteres?
Contém pelo menos uma letra maiúscula?
Contém pelo menos um número?

Percorra a string com for e use condicionais para verificar cada critério. 
Ao final, diga se a senha é forte (todos os critérios) ou fraca (faltou algum).
"""

senha = input("Digite a senha: ")
senha_forte = True 
criterios = []

if len(senha) >= 8:
    criterios.append("(+) A senha tem pelo menos 8 caracteres")    
else:
    senha_forte = False
    criterios.append("(-) A senha não tem pelo menos 8 caracteres")

if any(char.isupper() for char in senha):
    criterios.append("(+) A senha contém pelo menos uma letra maiúscula")
else:
    senha_forte = False
    criterios.append("(-) A senha não contém pelo menos uma letra maiúscula")

if any(char.isdigit() for char in senha):
    criterios.append("(+) A senha contém pelo menos um número")
else:
    senha_forte = False
    criterios.append("(-) A senha não contém pelo menos um número")

if senha_forte:
    print("A senha é forte")
else:
    print("A senha é fraca")

for criterio in criterios:
    print(criterio)