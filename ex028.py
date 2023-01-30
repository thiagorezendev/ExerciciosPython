import random
numPC = random.randint(1, 5)
numHU = int(input('Digite um numero: '))
if numHU == numPC:
    print('Parabens, voce acertou!')
else:
    print('Errou!')
print('O numero do PC era: {}'.format(numPC))