lado1 = int(input('Digite o valor do lado 1: '))
lado2 = int(input('Digite o valor do lado 2: '))
lado3 = int(input('Digite o valor do lado 3: '))

if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print('O triângulo não existe!')
else:
    print('O triângulo existe!')