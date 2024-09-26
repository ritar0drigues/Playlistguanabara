soma = 0
cont = 0

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        print('Parou o programa!')
        break
    soma += n
    cont += 1
    
print('A quantidade de números foi: {} e a soma deles foi: {}'.format(cont, soma))