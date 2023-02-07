i = 1
while True:
    num = int(input('Desejo saber a tabuada do número: '))
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {i * num}')
        i += 1
    print('--' * 18)
print('Obrigado pelo acesso!')