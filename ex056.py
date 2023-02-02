maisv = ''
velho = 0
idadet = 0
contm = 0
media = 0
for i in range(0, 4):
    print('--- Pessoa {} ---'.format(i+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M\F]: ')).strip()
    idadet += idade
    if i == 0 and sexo in 'Mm':
        maisv = nome
        velho = idade
    if sexo in 'Mm' and idade > velho:
        velho = idade
        maisv = nome
    if sexo in 'Fm' and idade < 20:
        contm += 1
media = idadet / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho é o {}, com {} anos de idade'.format(maisv, velho))
print('E tem {} mulheres com menos de 20 anos!'.format(contm))