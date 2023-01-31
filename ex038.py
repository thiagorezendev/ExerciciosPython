print('- Escreva 2 números para comparação -')
num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')