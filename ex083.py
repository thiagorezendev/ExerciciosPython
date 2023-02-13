frase = str(input('Digite a expressão: '))
pilha = []
for simb in frase:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append(')')

if len(pilha) % 2 == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')


# Jeito alternativo de ser feito
for simb in frase:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('c')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
