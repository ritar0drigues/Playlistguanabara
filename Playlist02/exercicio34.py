cont18 = 0
conthomens = 0
contmulher = 0

while True:
    print('Cadastro de pessoas')
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o Sexo: [M/F]').upper()

    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
        
    decisao = str(input('Deseja continuar? [S/N]')).upper()
    if decisao == 'N':
        print('Programa encerrado.')
        break

            
print('A quantidade de pessoas maiores de 18 anos: {}'.format(cont18))
print('A quantidade de homens cadastrados é: {}'.format(conthomens))
print('A quantidade de mulheres com idade menor que 20 anos: {}'.format(contmulher))

    

    