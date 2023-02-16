dados = dict()
geral = list()
cont = media = soma = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while dados['sexo'] not in 'MF':
        print('ERROR! Porfavor, digite apenas M ou F!')
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Idade: '))
    geral.append(dados.copy())
    cont += 1
    soma += dados['idade']
    des = str(input('Deseja continuar?[S/N] '))
    while des not in 'SsNn':
        print('ERROR! Responda apenas S ou N!')
        des = str(input('Deseja continuar?[S/N] '))
    if des in 'Nn':
        break
media = soma / cont
print('=+=' * 25)
print(geral)
print(f'A) Ao todo temos {cont} pessoas cadastradas')
print(f'B) A média de idade é de {media:.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
        print()
print(f'D) Lista de pessoas que estão com idade acima da média: ')
for p in dados:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print('<< ENCERRADO >>')