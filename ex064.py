soma = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Digite um número: '))
    cont += 1
    soma = soma + num
print('~' * 40)
print('Foram digitados {} números'.format(cont - 1))
print('A soma dos números digitados é igual a {}'.format(soma - 999))
print('~' * 40)
