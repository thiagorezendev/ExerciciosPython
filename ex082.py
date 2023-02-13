numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    des = ' '
    while des not in 'SNsn':
        des = str(input('Quer continuar?[S/N] '))
    if des in 'Nn':
        break
pares = []
impares = []
for pos, i in enumerate(numeros):
    if i % 2 == 0:
        pares.append(i)
    if i % 2 == 1:
        impares.append(i)
print('~' * 45)
print(f'Segue a lista completa dos valores: {numeros}')
print(f'Segue a lista dos valores pares: {pares}')
print(f'Segue a lista dos valores impares: {impares}')