aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
print(f'Nome = {aluno["nome"]}')
print(f'Média = {aluno["media"]}')
if aluno["media"] < 7:
    print('Situação = Reprovado')
else:
    print('Situação = Aprovado')