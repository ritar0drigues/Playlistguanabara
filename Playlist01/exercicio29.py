velocidade = int(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('O carro está sendo multado, e a multa é: {}R$'.format((velocidade-80)*7))
else: 
    print('Continue assim!')
          