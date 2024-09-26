casa = float(input('valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: R$'))
prestacao = casa / (anos * 12)

condicao = salario * 0.3
if prestacao > condicao:
    print('Emprestimo negado')
else:
    print('Emprestimo concedido')