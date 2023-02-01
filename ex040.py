nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('Média de {:.2}'.format(media))
if media < 5:
    print('Aluno reprovado!')
elif media >= 5 and media < 6.9:
    print('Aluno vai para a recuperação!')
else:
    print('Aluno aprovado!')