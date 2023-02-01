preco = float(input('Informe o valor das compras: R$'))
print('Selecione abaixo a forma de pagamento: ')
print('1 - À vista no dinheiro ou cheque (-10%)\n2 - À vista no cartão (-5%)\n3 - Até duas vezes no cartão\n4 - Três vezes ou mais no cartão (+20%)')
pagamento = int(input('Informe a condição de pagamento: '))
if pagamento == 1:
    total = preco - (preco * 0.10)
    print('O valor total das compras ficou em R${:.2f}.'.format(total))
elif pagamento == 2:
    total = preco - (preco * 0.05)
    print('O valor total das compras ficou em R${:.2f}.'.format(total))
elif pagamento == 3:
    total = preco
    print('O valor total das compras ficou em R${:.2f}.'.format(total))
elif pagamento == 4:
    total = preco + (preco * 0.20)
    print('O valor total das compras ficou em R${:.2f}.'.format(total))
else:
    print('Opção inválida. Tente novamente.')