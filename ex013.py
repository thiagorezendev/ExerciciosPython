salario = float(input('Qual eh o salario do funcionario? R$'))
novoSal = (salario * 15 / 100) + salario
print('O salario que antes era de R${}, com 15% de aumento passa a ser R${:.2f}.'.format(salario, novoSal))