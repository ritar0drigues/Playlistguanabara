nmr = int(input('Digite um número: '))
U = nmr // 1 % 10
D = nmr // 10 % 10
C = nmr // 100 % 10
M = nmr // 1000 % 10
print("A unidade vale: {}".format(U))
print("A dezena vale: {}".format(D))
print("A centena vale: {}".format(C))
print("O milhar vale: {}".format(M))