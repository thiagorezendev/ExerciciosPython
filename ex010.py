reais = float(input('Quantos reais voce tem? R$ '))
dolar = reais / 5.15
print('Com R${} voce pode comprar U${:.2f}'.format(reais, dolar))