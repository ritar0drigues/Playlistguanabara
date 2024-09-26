resultado1 = resultado2 = resultado3 = resultado4 = 0
print('Caixa Eletrônico')
valor = int(input('Digite o valor a ser sacado: '))

while valor > 0:
    
    if valor >= 50:
        resultado1 = valor // 50
        valor = valor % 50
        
    elif valor >=20:
        resultado2 = valor//20
        valor = valor % 20
        
    elif valor >= 10:
        resultado3 = valor//10
        valor = valor % 10
        
    elif valor >= 1:
        resultado4 = valor // 1
        valor = valor % 1
                
print('Serão entregues: {} notas de 50R$\n{} notas de 20 R$\n{} notas de 10 R$\n{} notas de 1R$.'.format(int(resultado1),int(resultado2),int(resultado3),int(resultado4)))
            