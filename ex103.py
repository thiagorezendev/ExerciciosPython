def ficha(nome='<desconhecido>', gols=0):
    if nome == '':
        print(f'O jogador <desconhecido> fez {gols}(s) no campeonato.')
    else:
        print(f'O jogador {nome} fez {gols}(s) no campeonato.')


print('_' * 30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric(): # Verifico se é numérico porque string permite deixar o input sem ler nada
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
