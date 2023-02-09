numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#num = 0
while True:
    cont = int(input('Digite um número entre 0 e 20: '))
    if 0 <= cont <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {numero[cont]}')
