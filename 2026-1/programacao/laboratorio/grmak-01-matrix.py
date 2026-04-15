import time
import random

def eh_par(numero):
    return numero % 2 == 0 

for i in range(1,8):
    if eh_par(i):
        print(f'{i} é par')
    else:
        print(f'{i} é ímpar')


def estatistica(a:int,b:int,c:int):
    soma=a+b+c
    media=soma/3
    maior=max(a,b,c)
    menor=min(a,b,c)
    return soma, media, maior, menor

s, m, mx, mn = estatistica('8',5,10)

print(f'Soma:{s} | Média:{m:.1f} | Maior:{mx} | Menor:{mn}')



def cor():
  verdes = ["\033[32m", "\033[38;5;22m", "\033[38;5;28m", "\033[38;5;34m", "\033[38;5;40m", "\033[38;5;46m", "\033[38;5;82m"]
  return random.randint(0, len(verdes)-1)


def fmatrix():
    matrix = ["."*20] * 10
    
    reset = "\033[0m"

    for i in range(1, len(matrix)):
        verdin = random.randint(0, len(verdes)-1)
        print(f"{verdes[verdin]}{matrix[i]}")
        time.sleep(1)

    print(f"{reset}")
        
    #print(matrix[1][0])    
    print(ord('a'))
    print(ord('z'))

    print(random.randint(1, 10))