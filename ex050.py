soma = 0
for i in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print('A soma dos pares = {}'.format(soma))