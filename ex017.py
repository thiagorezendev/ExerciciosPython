from math import hypot
catOposto = float(input('Digite o cateto oposto: '))
catAdj = float(input('Digite o cateto adjacente: '))
hipo = hypot(catAdj, catOposto)
print('A hipotenusa vai medir: {:.2f}'.format(hipo))

''' Sem importação:
    catOposto = float(input('Digite o cateto oposto: '))
    catAdj = float(input('Digite o cateto adjacente: '))
    hipo = (catAdj ** 2  + catOposto ** 2) ** (1/2)
    print('A hipotenusa vai medir: {:.2f}'.format(hipo))'''