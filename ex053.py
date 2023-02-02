frase = str(input('Verifique se é um palíndromo: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
print('Normal: {}\nInvertida: {}'.format(juntar, inverso))
if inverso == juntar:
    print('A frase é um palíndromo!')
else:
    print('Não é um palíndromo!')