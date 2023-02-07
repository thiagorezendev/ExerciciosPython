print('~' * 30)
print('        LOJAS TOTAL90')
print('~' * 30)
total = maiorM = menorP = cont = 0
barato = ' '
while True:
    nome = str(input('Nome do produto: '))
    preco = int(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        maiorM += 1
    if cont == 1:
        menorP = preco
        barato = nome
    else:
        if preco < menorP:
            menorP = preco
            barato = nome
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja adicionar compras? [S/N] ')).strip().upper()[0]
    if parar == 'N':
        break
print('        --- FIM DAS COMPRAS ---')
print(f'Suas compras ficaram no total de R${total:.2f}')
print(f'Temos {maiorM} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} custando apenas R${menorP:.2f}')