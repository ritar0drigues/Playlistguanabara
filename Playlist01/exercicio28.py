from random import randint
computador = randint(0,5)

nmr = int(input('Adivinhe o número entre 0 e 5: '))
if nmr == computador:
    print("Parabéns, você adivinhou o número {}".format(nmr))
else:
    print("Tente novamente!")
    