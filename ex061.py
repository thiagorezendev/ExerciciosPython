print('=' * 25)
print('  10 TERMOS DE UMA P.A')
print('=' * 25)
termo = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
ter = termo
cont = 1
while cont <= 10:
    print('{} -> '.format(ter), end='')
    ter += razao
    cont += 1
print('ACABOU')