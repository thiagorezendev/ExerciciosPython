galera = []
dados = []
maiorp = []
menorp = []
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    galera.append(dados[:])
    dados.clear()
    des = ' '
    while des not in 'SnsN':
        des = str(input('Quer continuar?[S/N] '))
    if des in 'Nn':
        break

print('~' * 45)
print(f'Foram cadastradas {len(galera)} pessoas')
print(f'O maior peso foi de {maiorpeso:.2f}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]' , end='')
print(f'\nO menor peso foi de {menorpeso:.2f}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menorpeso:
        print(f'[{p[0]}]', end='')
#print(galera)