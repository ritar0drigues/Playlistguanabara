from random import shuffle
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Tercerio nome: ")
n4 = input("Quarto alnuo: ")
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)