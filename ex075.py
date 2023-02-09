n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais número: '))
n4 = int(input('Digite o último número: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {numeros}')
if 9 in numeros:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
else:
    print('O valor 9 não apareceu nenhuma vez')
if 3 in numeros:
    print(f'O valor 3 foi digitado na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
