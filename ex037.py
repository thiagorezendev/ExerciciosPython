print('Escolha um número de acordo com o que deseja:')
print('1 - Conversão para binário')
print('2 - Conversão para octal')
print('3 - Conversão para hexadecimal')
num = int(input('Informe sua escolha: '))
numero = int(input('Digite um numero: '))
if num == 1:
    print('{} em binário fica {}'.format(numero, bin(numero)[2:]))
elif num == 2:
    print('{} em octal fica {}'.format(numero, oct(numero)[2:]))
elif num == 3:
    print('{} em hexadecimal fica {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')