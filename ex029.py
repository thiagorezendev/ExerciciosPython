velo = int(input('Digite a velocidade do carro: '))
if velo > 80:
    print('Você foi multado!')
    multa = (velo - 80) * 7
    print('E terá que pagar R${} de multa.'.format(multa))
