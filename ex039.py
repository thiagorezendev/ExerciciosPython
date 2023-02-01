from datetime import date
nascimento = int(input('Informe seu ano de nascimento: '))
ano = date.today().year
idade = ano - nascimento
if idade == 18:
    print('Está na hora de se alistar no exército!')
elif idade < 18:
    tempo = 18 - idade
    print('Ainda não chegou sua hora para alistamento militar! Faltam {} anos.'.format(tempo))
else:
    tempo = idade - 18
    print('Passaram-se {} anos do tempo de alistamento, aliste-se já!'.format(tempo))
