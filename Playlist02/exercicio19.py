from datetime import date
contmenor= 0
contmaior = 0
atual = date.today().year

for c in range(1,8):
    nasc = int(input("Digite o ano em que a pessoa nasceu: "))
    idade = atual - nasc
    if idade < 18:
        contmenor+=1
    elif idade >= 18:
        contmaior+=1
        
print("Há {} pessoas de menor e {} pessoas de maior".format(contmenor,contmaior))
