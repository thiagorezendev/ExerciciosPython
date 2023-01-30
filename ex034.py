sal = float(input('Escreva seu salário: '))
if sal <= 1250:
    aumento = sal + (sal * 0.15)
else:
    aumento = sal + (sal * 0.10)
print('Com o aumento, seu salário passa a ser R${:.2f}.'.format(aumento))