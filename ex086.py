matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('~' * 45)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


# Modo que eu fiz KKKKK
matriz = [[], [], []]
matriz[0].append(int(input(f'Digite um valor para [0, 0]: ')))
matriz[0].append(int(input(f'Digite um valor para [0, 1]: ')))
matriz[0].append(int(input(f'Digite um valor para [0, 2]: ')))
matriz[1].append(int(input(f'Digite um valor para [1, 0]: ')))
matriz[1].append(int(input(f'Digite um valor para [1, 1]: ')))
matriz[1].append(int(input(f'Digite um valor para [1, 2]: ')))
matriz[2].append(int(input(f'Digite um valor para [2, 0]: ')))
matriz[2].append(int(input(f'Digite um valor para [2, 1]: ')))
matriz[2].append(int(input(f'Digite um valor para [2, 2]: ')))
print('~' * 45)
print(f'[{matriz[0][0]:^5}][{matriz[0][1]:^5}][{matriz[0][2]:^5}]')
print(f'[{matriz[1][0]:^5}][{matriz[1][1]:^5}][{matriz[1][2]:^5}]')
print(f'[{matriz[2][0]:^5}][{matriz[2][1]:^5}][{matriz[2][2]:^5}]')
