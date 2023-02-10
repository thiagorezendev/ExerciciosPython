produtos = ('Notebook', 2540.00, 'Mesa gamer', 650.99, 'Gabinete', 100.00, 'Mouse G900', 870.90,
            'Monitor 244hz', 1230.99, 'Mousepad', 45.00, 'Manete Play4', 240.99, 'Caneta', 3.00)
print('=' * 40)
print(f'{"CARRINHO DE COMPRAS":^40}')
print('=' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>8.2f}')
print('=' * 40)

