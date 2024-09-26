distancia = float(input('Digite a distância de uma viagem: '))
if distancia <= 200:
    print('A passagem custa: {}'.format(distancia*0.50))
else:
    print('A passagem custa: {}'.format(distancia*0.45))
