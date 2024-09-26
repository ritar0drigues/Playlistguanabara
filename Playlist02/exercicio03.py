valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

if valor1 > valor2:
    print('O primeiro valor é maior.')
elif valor2 > valor1:
    print('O segundo valor é maior')
elif valor1 == valor2:
    print('Não existe valor maior, os dois são iguais.')
else: 
    print('Saindo da aplicação!')