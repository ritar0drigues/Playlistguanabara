from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opcões:
[0]PEDRA
[1]PAPEL
[2]TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 10)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('Empate!')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Jogador perdeu')
elif computador == 1:
    if jogador == 0:
        print('Jogador perdeu')
    elif jogador == 1:
        print('Empate!')
    elif jogador == 2:
        print('Jogador venceu')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Jogador perdeu')
    elif jogador == 2:
        print('Empate!')
else:
    print('Jogo encerrado')