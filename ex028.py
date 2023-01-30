import random
from time import sleep
numPC = random.randint(0, 5)
print('---' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinha-lo...')
print('---' * 20)
numHU = int(input('Em que número pensei: '))
print('Pensando...')
sleep(1.5)
if numHU == numPC:
    print('Parabens, voce acertou!')
else:
    print('Errou!')
print('O numero que eu pensei foi: {}'.format(numPC))