r1 = float(input('Digite o primeiro comprimento: '))
r2 = float(input('Digite o segundo comprimero: '))
r3 = float(input('Digite o terceiro comprimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')