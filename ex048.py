soma = 0
for i in range(1, 501):
    if i % 2 == 1:
        if i % 3 == 0:
            soma += i
print('{}'.format(soma))