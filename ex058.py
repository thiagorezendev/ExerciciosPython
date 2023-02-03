import random
from time import sleep
numPC = random.randint(0, 10)
print('---' * 19)
print('Vou pensar em um número de 0 a 10, tente adivinha-lo...')
print('---' * 19)
numHU = int(input('Em que número pensei: '))
while numPC != numHU:
    print('Pensando...')
    sleep(0.3)
    numHU = int(input('Não, diga outro '))
    if numHU == numPC:
        print('Parabens, você acertou!')
print('O numero que eu pensei foi: {}'.format(numPC))