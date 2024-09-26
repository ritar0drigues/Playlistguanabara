s = 0
for c in range(1,7):
    nmr = int(input('Digite um número: '))
    if nmr % 2 == 0:
        s = s + nmr

print('A soma dos números pares é: {}'.format(s))

