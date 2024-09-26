# nome = str(input('Qual é seu nome? '))
# if nome == 'Gustavo':
#     print('legal!')
# else:
#     print('Ah, sim')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m}')
if m >= 6.0:
    print('Parabéns, meu amor')
else:
    print('Que pena!')
