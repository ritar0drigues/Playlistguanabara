a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = a1
contador = 1
total = 0
mais = 10 
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} ->'.format(termo), end='')
        termo += r
        contador +=1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
