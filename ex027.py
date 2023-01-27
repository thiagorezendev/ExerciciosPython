nome = str(input('Digite seu nome completo: ')).strip()
name = nome.split()
print('Primeiro nome: {}'.format(name[0]))
print('Ultimo nome: {}'.format(name[len(name) - 1]))
