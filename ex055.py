maiorp = 0
for i in range(0, 5):
    peso = int(input('Informe o peso: KG'))
    menorp = peso
    if peso > maiorp:
        maiorp = peso
    if peso < menorp:
        menorp = peso
print('O maior peso foi: {}kg\nO menor peso foi: {}kg'.format(maiorp, menorp))