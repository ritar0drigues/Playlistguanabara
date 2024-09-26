import math
# catetop = float(input("Digite o valor do cateto oposto: "))
# ladop = math.pow(catetop,2)
# catetoadj = float(input("Digite o valor do cateto adjacente: "))
# ladoadj = math.pow(catetoadj,2)
# print("O valor da hipotenusa é {}".format(math.sqrt(ladop + ladoadj)))

catetop = float(input("Digite o valor do cateto oposto: "))
catetoadj = float(input("Digite o valor do cateto adjacente: "))
hi = math.hypot(catetop,catetoadj)
print("A hipotenusa mede {:.2f}".format(hi))