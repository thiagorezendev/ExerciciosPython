# Modo 'correto' de se fazer
numeros = [[], []]
num = 0
for c in range(0, 7):
    num = int(input(f'Digite o {c + 1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('~' * 45)
numeros[0].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
numeros[1].sort()
print(f'Os valores impares digitados foram: {numeros[1]}')


# Modo que eu fiz
todos = []
pares = []
impares = []
for c in range(0, 7):
    todos.append(int(input(f'Digite o {c + 1}º valor: ')))

for p in todos:
    if p % 2 == 0:
        pares.append(p)
    else:
        impares.append(p)
print('~' * 45)
pares.sort()
print(f'Os valores pares digitados foram: {pares}')
impares.sort()
print(f'Os valores impares digitados foram: {impares}')