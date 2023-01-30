dist = int(input('Digite a distância da viagem em km: '))
if dist <= 200:
    preco = 0.50 * dist
    print('Você irá pagar: R$ {:.2f}'.format(preco))
else:
    preco = 0.45 * dist
    print('Você irá pagar: R$ {:.2f}'.format(preco))