#lanche = ('Hamburguer', 'Suco', 'Pizza','Pudim')
# print(lanche)
# print(lanche[1])
# print(lanche[1:3])
# print(lanche[-2])
# print(lanche[-2:])
# print(lanche[2:])


# Tuplas são imutáveis
# lanche[1] = 'Refrigerante' não é possível alterar
# print(lanche[1])

# print(len(lanche))

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# É A MESMA COISA DE :
# for cont in range(0, len(lanche)):
#     print(f'{lanche[cont]} na posição {cont}')
# É A MESMA COISA DE: 
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posicão {pos}')

# Printar os elementos em ordem:
# print(sorted(lanche))
# print(lanche)

a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c) 
print(len(c))
print(c.count(2)) # quantas vezes aparece o número 2 na tupla c
print(c.index(8)) # indica a posição do elemento 8 na tupla c

print(c.index(2,1)) # indica a posição do elemento 2, a partir da priemira posição na tupla c

pessoa = ('Gustavo', 39, 'M', 99.88)
del(pessoa) # deletar uma pessoa, não há  como deletear um item da tupla
print(pessoa)

