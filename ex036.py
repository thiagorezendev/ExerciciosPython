casa = float(input('Valor da casa: R$'))
salario = float(input('Informe o seu salário: R$'))
anos = float(input('Informe em quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
execeder = salario * 0.30
if prestacao > execeder:
    print('Empréstimo negado! Pois valor da prestação excede 30% do seu salário.')
else:
    print('Empréstimo aceito!')
print('Valor da prestação: {:.2f}.'.format(prestacao))