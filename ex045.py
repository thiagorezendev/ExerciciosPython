import random
print('Bem vindo ao JokenPo! Veja se consegue ganhar de mim.')
print('Escolha entre: Pedra, Papel ou Tesoura')
pcesc = random.choice(['Pedra', 'Papel', 'Tesoura'])
esc = str(input('Informe o escolhido: '))
if pcesc == 'Pedra' and esc == 'Papel':
    print('Parabéns, você ganhou!')
elif pcesc == 'Pedra' and esc == 'Tesoura':
    print('Não deu, ganhei de você!')
elif pcesc == 'Papel' and esc == 'Pedra':
    print('Não deu, ganhei de você!')
elif pcesc == 'Papel' and esc == 'Tesoura':
    print('Parabéns, você ganhou!')
elif pcesc == 'Tesoura' and esc == 'Pedra':
    print('Parabéns, você ganhou!')
elif pcesc == 'Tesoura' and esc == 'Papel':
    print('Não deu, ganhei de você!')
else:
    print('Empatamos!')
#print('{}'.format(pcesc))