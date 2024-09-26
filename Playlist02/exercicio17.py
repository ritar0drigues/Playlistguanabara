count = 0
nmr = int(input('Digite um número: '))
for c in range(1,nmr+1):
    if nmr % c == 0:
        count+=1
if count > 2:
    print('O número não é primo')
else:
    print('O número é primo')