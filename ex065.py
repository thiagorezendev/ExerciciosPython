maior = cont = soma = menor = 0
des = ''
while des != 'N':
    num = int(input('Digite um valor: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    des = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
media = soma / cont
print('~' * 40)
print('A media dos valores digitados foi de {:.2f}'.format(media))
print('O maior valor digitado foi {}\nO menor valor digitado foi {}'.format(maior, menor))
