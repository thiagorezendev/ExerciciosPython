import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
print('Bem vindo ao JoKenPo!')
print('''Suas opções:
 0 - Pedra
 1 - Papel
 2 - Tesoura''')
esc = int(input('Qual você escolhe: '))
pcesc = random.randint(0, 2)
print('JO!')
time.sleep(0.5)
print('KEN!')
time.sleep(0.5)
print('PO!')
time.sleep(0.5)
print('+=+=' * 6)
print('Jogador jogou {}\nComputador jogou {}'.format(itens[esc], itens[pcesc]))
print('+=+=' * 6)
if pcesc == 0 and esc == 1:
    print('Parabéns, você ganhou!')
elif pcesc == 0 and esc == 2:
    print('Não deu, ganhei de você!')
elif pcesc == 1 and esc == 0:
    print('Não deu, ganhei de você!')
elif pcesc == 1 and esc == 2:
    print('Parabéns, você ganhou!')
elif pcesc == 2 and esc == 0:
    print('Parabéns, você ganhou!')
elif pcesc == 2 and esc == 1:
    print('Não deu, ganhei de você!')
else:
    print('Empatamos!')





















'''print('Bem vindo ao JokenPo! Veja se consegue ganhar de mim.')
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
    print('Empatamos!')'''
#print('{}'.format(pcesc))