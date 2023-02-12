numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não irei adicionar...')
    des = ' '
    while des not in 'SN':
        des = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if des == 'N':
        break
print('+=+' * 10)
print(f'Os valores digitados foram {sorted(numeros)}')