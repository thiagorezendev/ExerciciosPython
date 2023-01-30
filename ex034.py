sal = float(input('Escreva seu salário: '))
if sal > 1.250:
    salnovo = sal * 0.10
    aumento = sal + salnovo
else sal <= 1.250:
    salnovo = sal * 0.15
    aumento = sal + salnovo
print('Com o aumento, seu salário passa a ser R${:.2f}.'.format(aumento))