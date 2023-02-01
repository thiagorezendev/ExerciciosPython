from datetime import date
print(' - Informe o ano de nascimento para saber a categoria - ')
nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: JUVENIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')