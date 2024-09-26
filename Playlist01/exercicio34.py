salario = float(input('Digite o valor do salário:'))
if salario <= 1250:
    novo = salario + (salario * 15/ 100)
    print("O novo salário é: {}".format(novo))
else:
    novo = salario + (salario* 10 /100)
    print("O novo salário é: {}".format(novo))