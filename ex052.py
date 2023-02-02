div = 0
num = int(input('Digite um numero: '))
for i in range(1, num + 1):
    if num % i == 0:
        div += 1
if div == 2:
    print('O número é primo!')
else:
    print('O número não é primo!')