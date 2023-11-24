#ATIVIDADE4

'''As variáveis de tipo string possuem uma série de funcionalidades já
implementadas e seus caracteres e substrings podem ser acessados usando
indexação e slicing. Crie um exemplo onde:
○ Declare uma variável nome atribuindo a ela seu nome completo;
○ Pesquise por funcionalidades já implementadas nas strings e separe
em duas variáveis novas seu nome do seu sobrenome;
○ Verifique qual das duas novas variáveis antecede a outra na ordem
alfabética;
○ Verifique a quantidade de caracteres de cada uma das novas variáveis;
○ Verifique se seu nome é uma palíndromo;'''

# Declare uma variável nome atribuindo a ela seu nome completo
nome_completo = "John Doe"

# Pesquise por funcionalidades já implementadas nas strings e separe em duas variáveis novas seu nome do seu sobrenome
# Note: O exemplo assume que o nome e sobrenome são separados por um espaço
nome, sobrenome = nome_completo.split()

# Verifique qual das duas novas variáveis antecede a outra na ordem alfabética
if nome < sobrenome:
    print(f"{nome} precede {sobrenome} na ordem alfabética.")
elif nome > sobrenome:
    print(f"{sobrenome} precede {nome} na ordem alfabética.")
else:
    print("Os nomes são iguais.")

# Verifique a quantidade de caracteres de cada uma das novas variáveis
print(f"Quantidade de caracteres em 'nome': {len(nome)}")
print(f"Quantidade de caracteres em 'sobrenome': {len(sobrenome)}")

# Verifique se seu nome é uma palíndromo
if nome == nome[::-1]:
    print(f"{nome} é um palíndromo.")
else:
    print(f"{nome} não é um palíndromo.")
