ano = int(input('Digite um ano para saber se ele é bissexto ou nao: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano de {} não é bissexto!'.format(ano))