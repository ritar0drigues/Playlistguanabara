cont = 0
soma = 0
while True:
    nmr = int(input('Valor: '))
    if nmr == 999:
        print('Parada do programa.')
        break
    cont +=1
    soma += nmr
print('Foram digitados {} números e a soma foi: {}'.format(cont,soma))
    