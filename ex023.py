num = int(input('Digite um numero: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(unidade, dezena, centena, milhar))