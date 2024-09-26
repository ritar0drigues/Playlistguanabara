valor = int(input('Digite um numero inteiro: '))
print('Escolha uma das abses para conversão:\n[1] converter para binário\n[2] converter para octal\n[3] converter para hexadecimal ')
op = int(input('Digite sua opcão: '))
if op ==1:
    print('{} convertido para BINARIO é igual a {}'.format(valor, bin(valor)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(valor,oct(valor)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(valor, hex(valor)[2:]))
else:
    print('Saindo da aplicação!')
    