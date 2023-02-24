from time import sleep
def maior(* num):
    print('-=-' * 10)
    print('Analisando os valores passados...')
    tam = len(num)
    c = mai = 0
    for n in num:
        print(f'{n} ', end='')
        sleep(0.5)
        if c == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        c += 1
    print(f'Foram informados {tam} valores ao todos.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
