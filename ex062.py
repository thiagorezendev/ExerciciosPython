print('=' * 25)
print('  10 TERMOS DE UMA P.A')
print('=' * 25)
termo = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
ter = termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(ter), end='')
        ter += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja mostrar mais quantos termos? '))
print('Progressão finalizada com {} termos mostrado'.format(total))