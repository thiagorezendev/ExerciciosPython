from random import randint
from time import sleep
from operator import itemgetter
i = 1
ranking = list()
jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'    O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores: ')
for k, v in enumerate(ranking):
    print(f'    {k + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
