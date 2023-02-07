maior = homens = mulher20 = 0
while True:
    print('--- CADASTRAR PESSOAS ---')
    ida = int(input('Idade: '))
    sex = ' '
    while sex not in 'FM':
        sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if ida >= 18:
        maior += 1
    if sex == 'M':
        homens += 1
    if ida < 20 and sex == 'F':
        mulher20 += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if parar == 'N':
        break
print('--- FIM DO PROGRAMA ---')
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulher20} mulheres com menos de 20 anos')