"""
Exercício 19 - Jogo de Adivinhação
Crie um jogo onde o computador “pensa” em um número de 1 a 50 (use random.randint(1, 50)). 
O jogador tem 7 tentativas para acertar. A cada tentativa, informe se o palpite é maior ou menor que o número secreto. 
Ao final, classifique:

Acertou em até 3 tentativas: MESTRE!
Acertou em 4 a 5 tentativas: Muito bom!
Acertou em 6 a 7 tentativas: Na hora certa!
Não acertou: Game Over!"""

import random

numero_secreto = random.randint(1, 50)
tentativas = 0

while tentativas < 7:
    palpite = int(input("Digite um número entre 1 e 50: "))
    tentativas += 1
    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior que o palpite.")
    else:
        print("O número secreto é menor que o palpite.")
