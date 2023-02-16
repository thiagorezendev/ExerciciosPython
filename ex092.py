from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratacao'] - ano) + 35
print("=" * 40)
for k, v in pessoa.items():
    print(f'    - {k} tem o valor {v}')
