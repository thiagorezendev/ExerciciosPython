print('Selecione abaixo a forma de pagamento: ')
print('1 - À vista no dinheiro ou cheque\n2 - À vista no cartão\n3 - Até duas vezes no cartão\n4 - Três vezes ou mais no cartão')
pagamento = int(input('Informe a condição de pagamento: '))
preco = float(input('Informe o valor do produto: '))
if pagamento == 1:
    total = preco - (preco * 0.10)
elif pagamento == 2:
    total = preco - (preco * 0.05)
elif pagamento == 3:
    total = preco
elif pagamento == 4:
    total = preco + (preco * 0.20)
print('O valor total do produto ficou em R${:.2f}.'.format(total))