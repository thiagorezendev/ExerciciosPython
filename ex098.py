from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1 # Transformando em positivo
    if passo == 0:
        passo = 1

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.5)

    if inicio < fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='')
            c += passo
            sleep(0.5)
        print('FIM!')
    else:
        c = inicio
        while c >= fim:
            print(f'{c} ', end='')
            c -= passo
            sleep(0.5)
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)