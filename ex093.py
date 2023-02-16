dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
i = gol = 0
while i < partidas:
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    i += 1
dados['gols'] = gols[:]
dados['total'] = sum(gols)
print('~' * 50)
print(dados)
print('~' * 50)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('~' * 50)
print(f'O {dados["nome"]} jogou {partidas} partidas:')
for pos, g in enumerate(gols):
    print(f'    => Na partida {pos + 1}, fez {g} gols')
print(f'Foi um total de {dados["total"]} gols')