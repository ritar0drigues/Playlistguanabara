print('Bem vindo ao programa!')
nmr1 = int(input("Digite o primeiro número: "))
nmr2 = int(input("Digite o segundo número: "))
op = 0

while op != 5:
    print('-=' * 10)

    print('M E N U')
    print("1.Somar\n2.Multiplicar\n3.Maior Valor\n4.Novos números\n5.Sair do programa")

    print('-=' * 10)

    op = int(input("Digite a opção desejada: "))
    
    if op == 1:
        resultado = nmr1 + nmr2
        print('A soma dos números é: {}'.format(resultado))
        
        
    elif op == 2:
        resultado = nmr1 * nmr2
        print('A multiplicação dos números é {}'.format(resultado))
        
        
    elif op == 3:
        if nmr1 > nmr2:
            print('O maior número é: {}'.format(nmr1))
            
        elif nmr1 < nmr2:
            print('O maior número é: {}'.format(nmr2))
        
        else:
            print('Os números são iguais.')
            

    elif op == 4:
        nmr1 = int(input('Digite o novo valor: '))      
        nmr2 = int(input('Digite o novo valor: ')) 
           
        
    elif op == 5:
        print('Saindo do programa...')
        
        
    else:
        print('Opção inválida, tente novamente!')  
        

        