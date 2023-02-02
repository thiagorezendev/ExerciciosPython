from datetime import date
maior = 0
menor = 0
atual = date.today().year
for i in range(0, 7):
    ano = int(input('Ano de nascimento: '))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são de maior\n{} pessoas são de menor'.format(maior, menor))