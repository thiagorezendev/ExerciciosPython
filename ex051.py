print('=' * 25)
print('  10 TERMOS DE UMA P.A')
print('=' * 25)
termo = int(input('Primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print('{}'.format(i), end=' -> ')
print('ACABOU')