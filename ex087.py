matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somater = valsegunda = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz[l][2]:
            somater += matriz[l][2]

print('~' * 45)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('~' * 45)
print(f'Soma dos valores pares digitados: {soma}')
print(f'Soma dos valores da terceira coluna: {somater}')
for c in range(0, 3):
        if c == 0:
            valsegunda = matriz[1][c]
        else:
            if valsegunda < matriz[1][c]:
                valsegunda = matriz[1][c]
print(f'O maior valor da segunda linha: {valsegunda}')
