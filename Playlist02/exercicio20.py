maiorpeso = 0
menorpeso = 0
for l in range(1,6):
    peso = (float(input("Digite o peso da {}ª pessoa: ".format(l))))
    if peso > maiorpeso:
        maiorpeso = peso
        menorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
        
print("O maior peso foi de {}kg e o menor foi de {}kg".format(maiorpeso,menorpeso))
    
    