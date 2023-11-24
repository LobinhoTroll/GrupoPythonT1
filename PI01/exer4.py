# Declare uma variável nome atribuindo a ela seu nome completo
nome_completo = "Seu Nome Completo"

# Separe em duas variáveis novas seu nome do seu sobrenome
nome, sobrenome = nome_completo.split()

# Verifique qual das duas novas variáveis antecede a outra na ordem alfabética
if nome < sobrenome:
    print(f"{nome} antecede {sobrenome} na ordem alfabética.")
else:
    print(f"{sobrenome} antecede {nome} na ordem alfabética.")

# Verifique a quantidade de caracteres de cada uma das novas variáveis
len_nome = len(nome)
len_sobrenome = len(sobrenome)

print(f"{nome} tem {len_nome} caracteres.")
print(f"{sobrenome} tem {len_sobrenome} caracteres.")

# Verifique se seu nome é uma palíndromo
if nome == nome[::-1]:
    print(f"{nome} é um palíndromo!")
else:
    print(f"{nome} não é um palíndromo.")
