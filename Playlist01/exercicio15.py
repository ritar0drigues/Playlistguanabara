km = float(input('Digite quantos quilometros: '))
valorkm = km * 0.15
dia = int(input('Digite a qtd de dias: '))
valordias = dia * 60

print('O total a pagar, considerando {} km e {} dia(s), é: {}'.format(km,dia,(valorkm+valordias)))