nome_completo = "Felipe Gregue"

partes_nome = nome_completo.split()

if len(partes_nome) >= 2:
    primeiro_nome = partes_nome[0]
    sobrenome = ' '.join(partes_nome[1:])  

    print("Primeiro Nome:", primeiro_nome)
    print("Sobrenome:", sobrenome)
else:
    print("Erro: Nome completo deve ter pelo menos um nome e um sobrenome.")

if primeiro_nome < sobrenome:
    print(f"{primeiro_nome} vem antes de {sobrenome} na ordem alfabética.")
elif primeiro_nome > sobrenome:
    print(f"{primeiro_nome} vem depois de {sobrenome} na ordem alfabética.")
else:
    print(f"{primeiro_nome} e {sobrenome} são iguais na ordem alfabética.")

tamanho_primeiro_nome = len(primeiro_nome)
tamanho_sobrenome = len(sobrenome)

print(f"Quantidade de caracteres em {primeiro_nome}: {tamanho_primeiro_nome}")
print(f"Quantidade de caracteres em {sobrenome}: {tamanho_sobrenome}")

nome = "Felipe"

nome_formatado = nome.lower()

if nome_formatado == nome_formatado[::-1]:
    print(f"{nome} é um palíndromo.")
else:
    print(f"{nome} não é um palíndromo.")


