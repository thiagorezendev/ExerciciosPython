from time import sleep
valora = int(input('Digite o primeiro valor: '))
valorb = int(input('Digite o segundo valor: '))
maior = 0
escolha = 0
while escolha != 5:
    print('=' * 27)
    print('''    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos números
    [5] - Sair''')
    escolha = int(input('Digite o número escolhido: '))
    if escolha == 1:
        soma = valora + valorb
        print('A soma dos dois valores equivale a {}'.format(soma))
    elif escolha == 2:
        multi = valora * valorb
        print('O resultado da multiplicação dos valores é igual a {}'.format(multi))
    elif escolha == 3:
        if valora > valorb:
            maior = valora
            print('O maior dos dois valores é o {}'.format(maior))
        elif valorb > valora:
            maior = valorb
            print('O maior dos dois valores é o {}'.format(maior))
        elif valora == valorb:
            print('Os dois valores são iguais')
    elif escolha == 4:
        valora = int(input('Digite novos valores, primeiro valor: '))
        valorb = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Obrigado pelo acesso!')
        break
    else:
        print('Opção inválida! Tente novamente.')
    sleep(1)
