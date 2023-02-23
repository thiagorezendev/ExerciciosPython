def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area}m²')


print('Controle de Terrenos')
print('_' * 20)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)