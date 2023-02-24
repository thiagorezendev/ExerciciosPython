from random import randint
from time import sleep
valores = list()
def sorteio():
    for i in range(0, 5):
        valores.append(randint(1, 100))
    print('Sorteando 5 valores da lista: ', end='')
    for i in valores:
        print(f'{i} ', end='')
        sleep(0.5)
    print('PRONTO!')
def somaPar():
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {valores}, temos {soma}')

sorteio()
somaPar()

# Como eu fiz, maneira muito complicada KKKKK
'''def sorteio():
    print('Sorteando 5 valores da lista: ', end='')
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    num3 = randint(1, 100)
    num4 = randint(1, 100)
    num5 = randint(1, 100)
    valores.append(num1)
    valores.append(num2)
    valores.append(num3)
    valores.append(num4)
    valores.append(num5)
    for n in valores:
        print(f'{n} ', end='')
        sleep(0.5)
    print('PRONTO!')'''