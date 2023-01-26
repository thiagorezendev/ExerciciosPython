import random
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome4, nome3, nome2, nome1]
sorteado = random.choice(lista)
print('O aluno escolhido foi',sorteado)