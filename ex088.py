from random import randint
from time import sleep
print(f'=+' * 15)
print(f'{"MEGA SENA":^30}')
print(f'=+' * 15)
lista = []
total = []
quant = int(input('Quantidade de jogos que deseja: '))
i = 0
while i < quant:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    total.append(lista[:])
    lista.clear()
    i += 1
print(f'=+' * 5, f'SORTEANDO {quant} JOGOS', '=+' * 5)
for pos, l in enumerate(total):
    print(f'Jogo {pos + 1}: {l}')
    sleep(0.8)
print(f'=+' * 6, f'<BOA SORTE>', '=+' * 6)


# Modo que eu fiz (os numeros sorteados se repetem) :/
print(f'=+' * 15)
print(f'{"MEGA SENA":^30}')
print(f'=+' * 15)
quant = int(input('Quantidade de jogos que deseja: '))
i = 0
print(f'=+' * 5, f'SORTEANDO {quant} JOGOS', '=+' * 5)
jogos = []
while i < quant:
    sorteio = [randint(1, 61) for n in range(6)]
    sorteio.sort()
    print(f'Jogo {i + 1}: {sorteio}')
    i += 1
    sleep(0.5)
print(f'=+' * 6, f'<BOA SORTE>', '=+' * 6)