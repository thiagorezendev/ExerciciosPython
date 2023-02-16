dados = dict()
gols = list()
galera = list()
while True:
    print('-' * 30)
    dados['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    i = gol = 0
    gols.clear()
    while i < partidas:
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
        i += 1
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    galera.append(dados.copy())
    des = ' '
    while des not in 'SsnN':
        des = str(input('Quer continuar?[S/N] '))[0]
    if des in 'Nn':
        break
print('~' * 50)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(galera):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 interrompe) '))
    if busca == 999:
        break
    if busca >= len(galera):
        print(f'Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {galera[busca]["nome"]} -- ')
        for i, g in enumerate(galera[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols')
    print('-' * 40)
print('< VOLTE SEMPRE >')
