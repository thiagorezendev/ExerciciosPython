num = int(input('Qual numero deseja saber o fatorial? '))
num1 = num
fator = 1
print('{}! = '.format(num), end='')
while num1 > 0:
    print('{}'.format(num1), end='')
    print(' x ' if num1 > 1 else ' = ', end='')
    fator *= num1
    num1 -= 1
print('{}'.format(fator))