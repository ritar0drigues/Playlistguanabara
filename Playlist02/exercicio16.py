ptermo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão: '))
decimo = ptermo + (10 - 1) * razao
for c in range(ptermo, decimo + razao, razao):
    print('{}'.format(c), end= '-> ')
print('Acabou!')