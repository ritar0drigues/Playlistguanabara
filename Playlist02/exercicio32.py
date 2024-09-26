while True:
    n = int(input('Digite o número que deseja ver sua tabuada: '))
    if n < 0:
        print('Número negativo, saindo do programa!')
        break
    for c in range(0,11):
        print('{} x {} = {}'.format(n,c,(n*c)))
    
    
    