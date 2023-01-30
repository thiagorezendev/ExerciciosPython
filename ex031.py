dist = int(input('Digite a distância da viagem em km: '))
if dist <= 200:
    preco = 0.50 * dist
else:
    preco = 0.45 * dist
print('Você irá pagar: R$ {:.2f}'.format(preco))

# preco = dist * 0.50 if dist <= 200 else dist * 0.45