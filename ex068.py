from random import randint
print('=' * 19)
print(' PAR OU ÍMPAR JOGO')
print('=' * 19)
vit = 0
while True:
    n = int(input('Digite um valor: '))
    s = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    pc = randint(0, 10)
    soma = n + pc
    if soma % 2 == 0:
        print('~' * 45)
        print(f'Você jogou {n} e o PC {pc}. Total de {soma} deu par!')
        if s == 'P':
            print('Você venceu!')
            vit += 1
        if s == 'I':
            print('Você perdeu!')
            break
    if soma % 2 == 1:
        print('~' * 45)
        print(f'Você jogou {n} e o PC {pc}. Total de {soma} deu ímpar!')
        if s == 'I':
            print('Você venceu!')
            vit += 1
        if s == 'P':
            print('Você perdeu!')
            break
print(f'GAMER OVER! Você venceu {vit} vezes.')