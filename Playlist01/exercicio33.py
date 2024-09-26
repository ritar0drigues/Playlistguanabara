a = int(input("Digite o primeiro nmr: "))
b = int(input("Digite o primeiro nmr: "))
c = int(input("Digite o primeiro nmr: "))

menor = a
if b < a and b < c:
    menor = b
    print(menor)
if c < a and c < b:
    menor = c
    print(menor)