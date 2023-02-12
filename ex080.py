numeros = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0:
        numeros.append(n)
        print('Adicionado no final da lista...')
    elif n > numeros[-1]:
        numeros.append(n)
        print('Adicionado no final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('~' * 40)
print(f'Os valors digitados em ordem foram {numeros}')

