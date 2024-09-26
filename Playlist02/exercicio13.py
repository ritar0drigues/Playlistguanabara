s = 0
c = 0
for n in range(1,501):
    if n % 2 != 0 and n % 3 == 0:
        print(n)
        s = s + n
        c += 1
print('A soma de todos os {} números é {}'.format(c, s))