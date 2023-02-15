from time import sleep
alunos = []
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    des = ' '
    while des not in 'SnsN':
        des = str(input('Quer continuar?[S/N] '))
    if des in 'Nn':
        break
print(f'{"N.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('-' * 30)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 para encerrrar) '))
    if mostrar == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    if mostrar <= len(alunos) - 1:
        print(f'As nota de {alunos[mostrar][0]} foram {alunos[mostrar][1]}')
    print('-' * 30)

#print(f'{media}')
#for i, l in enumerate(alunos):
    #print(f'{i} {l}')
#print(f'{alunos}')
#print(f'{notas}')