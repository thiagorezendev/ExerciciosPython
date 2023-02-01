print('- Calculo de IMC -')
peso = float(input('Informe o peso: KG '))
alt = float(input('Informe a altura: M '))
imc = peso / (alt * 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Se encontra abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Se encontra sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Está obeso.')
else:
    print('Obesidade mórbida.')