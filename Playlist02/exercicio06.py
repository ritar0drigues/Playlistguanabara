from datetime import date
atual = date.today().year
ano = int(input('Digite o ano: '))
condicao = atual - ano
if condicao <= 9:
    print('Mirim')
elif condicao > 9 and condicao <= 14:
    print('Infantil')
elif condicao > 14 and condicao <= 19:
    print('Junior')
elif condicao > 19 and condicao <= 25:
    print('Senior')
elif condicao > 25:
    print('Master')