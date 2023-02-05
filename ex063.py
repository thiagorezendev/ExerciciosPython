print('-----' * 5)
print(' Sequência de Fibonacci')
print('-----' * 5)
num = int(input('Quantos termos voce quer mostrar: '))
n1 = 0
n2 = 1
print('{} - {} -'.format(n1, n2), end='')
i = 3
while i <= num:
    n3 = n1 + n2
    print(' {} -'.format(n3), end='')
    n1 = n2
    n2 = n3
    i += 1
print(' FIM')