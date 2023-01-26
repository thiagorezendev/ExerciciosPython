from random import shuffle
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome4, nome3, nome2, nome1]
shuffle(lista)
print('A ordem de apresentação sera:')
print(lista)