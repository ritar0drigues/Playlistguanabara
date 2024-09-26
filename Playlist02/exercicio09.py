produto = float(input('Digite o valor de um produto: '))
pagamento = int(input('Digite a forma de pagamento:\n[1]à vista\n[2]2x no cartão\n[3]3x ou mais no cartão: '))
if pagamento == 1:
    op = int(input('1 - Dinheiro/cheque\n2- No cartão: '))
    if op == 1:
        produto = produto * 0.9
        print('O produto irá custar: {:.2f}'.format(produto))
    elif op == 2:
        produto = produto * 0.95
        print('O produto irá custar: {:.2f}'.format(produto))
if pagamento == 2:
    print('A parcela do produto irá custar: {:.2f}, pois o produto manterá seu preço'.format(produto/2))
if pagamento == 3:
    produto = produto * 1.20
    print('O produto irá custar: {:.2f}'.format(produto)) 
