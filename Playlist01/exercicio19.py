import random
num1 = input("Digite o nome do primeiro aluno: ")
num2 = input("Digite o nome do segundo aluno: ")
num3 = input("Digite o nome do terceiro aluno: ")
num4 = input("Digite o nome do quarto aluno: ")
lista = [num1,num2,num3,num4]
resultado = random.choice(lista)
print("O aluno escolhido foi {}".format(resultado))