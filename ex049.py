num = int(input('Digite um número e veja sua tabuada: '))
print('---------------')
for i in range(1, 11):
    print('{} x {} = {}'.format(num, i, num * i))
print('---------------')
