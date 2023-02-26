from datetime import datetime
def voto(ano):
    atual = datetime.now().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: VOTO NEGADO!')
    elif 16 < idade < 65:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO!')
    else:
        print(f'Com {idade} anos: VOTO OPCIONAL!')


ano = int(input('Em que ano você nasceu: '))
voto(ano)