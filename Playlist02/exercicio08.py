

peso = float(input('Digite o peso: Kg  '))
altura = float(input('Digite a altura: m  '))
imc = peso / (altura ** 2)
print('O imc desta pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('Obesidade!')
elif(imc > 40):
    print('Obesidade mórbida')
else:
    print('Vai com Deus!')