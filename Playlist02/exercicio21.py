media = 0
cont = 0
maioridade = 0
for c in range(0,4):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = (input("Digite F - Feminino, M - Masculino: "))
    media = media + idade
    
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        homem = nome
    
    if sexo == 'F' and idade < 20:
        cont+=1
        
print("A média do grupo é: {}".format(media/4))
print("O nome do homem mais velho é: {}".format(homem))
print("A quantidade de mulheres é: {}".format(cont))