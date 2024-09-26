from random import randint
computador = randint(0,10)

print('Vamos jogar par ou impar: ')

jogador = int(input('Digite um número: '))
decisao = input('Par ou Ímpar? [P/I]').upper()
soma = jogador + computador

if soma % 2 == 0:
    resultado = 'P'
else:
    resultado = 'I'
    
print('Você jogou {} e o computador jogou {}. Total deu {}, {}'.format(jogador, computador, soma, 'Par' if resultado == 'P' else 'Ímpar'))

if decisao == resultado:
    print('Parabéns, você venceu.')
    
else:
    print('Que pena, você perdeu.')