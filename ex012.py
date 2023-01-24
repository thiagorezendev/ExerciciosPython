preco = float(input('Qual o preco do produto? R$'))
desconto = preco * 5 / 100
precoFim = preco - desconto
print('O preco era de R${}, com desconto de 5% ficou por R${:.2f}'.format(preco, precoFim))