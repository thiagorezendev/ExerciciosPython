numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    des = ' '
    while des not in 'SNsn':
        des = str(input('Quer continuar?[S/N] '))
    if des in 'Nn':
        break
print('~' * 45)
print(f'Você digitou {len(numeros)} elementos.')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')