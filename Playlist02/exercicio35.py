totalgasto = 0
contprod1000 = 0
menorvalor = cont = 0
produto = ''
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço de um produto: '))
    cont+=1
    totalgasto += preco
   
    if preco > 1.000:
        contprod1000+=1
    
    if cont == 1 or preco < menorvalor:
        menorvalor = preco
        produto = nome
            
    decisao = input('Deseja continuar com a compra? [S/N]: ')
    if decisao == 'N':
        break
        
        
print('O total gasto na compra é: {}'.format(totalgasto))
print('A quantidade de produtos que custam mais de 1000 R$ é: {}'.format(contprod1000))
print('O nome do produto mais barato é: {}'.format(produto))