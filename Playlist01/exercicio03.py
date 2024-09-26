# valor01 = int(input("Digite o primeiro valor: "))
# valor02 = int(input("Digite o segundo valor: "))
# soma = valor01 + valor02
# print(f"A soma entre {valor01} e {valor02} é:{soma}")



valor = input("Digite algo: ")
print(type(valor))

print("Valor é númerico? ", valor.isnumeric())

print("valor é alfabetico?", valor.isalpha())

print("valor é alfanumerico?", valor.isalnum())

print("valor está entre 0 e  127 da tabela ASCII?")
print(valor.isascii())

print("valor é decimal?")
print(valor.isdecimal())

print("valor é dígito?")
print(valor.isdigit())

print("valor é um indetificador válido? (não pode começar com número)")
print(valor.isidentifier())

print("valor está minusculo?")
print(valor.islower())

print("valor é imprimivel?(não é string vazia)")
print(valor.isprintable())

print("valor é espaço em branco?")
print(valor.isspace())

print("valor é título?(primeira letra maiúscula)")
print(valor.istitle())

print("valor é todo maiúsculo?")
print(valor.isupper())
