numeros = list()
maior = menor = 0
for i in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]

print('=' * 33)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for pos, n in enumerate(numeros):
    if n == maior:
        print(f'{pos}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for pos, n in enumerate(numeros):
    if n == menor:
        print(f'{pos}... ', end='')