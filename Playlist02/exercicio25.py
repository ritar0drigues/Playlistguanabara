# from math import factorial
# n = int(input('Digite um número para calcular seu fatorial: '))
# f = factorial(n)
# print("O fatorial de {} é: {}".format(n,f))


# n = int(input('Digite um número para calcular seu fatorial: '))
# c = n
# f = 1
# print('Calculando {}!'.format(n),end='')

# while c > 0:
#     print('{}'.format(c), end= '')
#     print(' x ' if c > 1 else ' = ', end= '')
#     f *= c
#     c -= 1
# print('{}'.format(f))

n = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1

print(f'Calculando {n}!', end=' ')

for i in range(n, 0, -1):
    print(i, end=' ')
    if i > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    fatorial *= i

print(fatorial)

