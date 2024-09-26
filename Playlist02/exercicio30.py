cont = 0
soma = 0
maior = 0
menor = 0


while True:
    valor = int(input('Digite um número: '))
    
    if cont == 0:
        maior = valor
        menor = valor
    
    else:
        if valor > maior:
            maior = valor
            
        if valor < menor:
            menor = valor
            
    soma += valor    
    cont+=1
    
        
    op = int(input('Deseja continuar?\n1.Sim\n2.Não\n'))
    if op == 2:
        break

media = (soma/cont)

print('O maior valor foi: {}'.format(maior))
print('O menor valor foi: {}'.format(menor))
print('A media dos valores foi: {}'.format(media))
 
    
    