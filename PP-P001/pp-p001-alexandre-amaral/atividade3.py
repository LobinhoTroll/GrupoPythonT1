

#ATIVDADE 3.1
'''Os caracteres numéricos aparecem na tabela ASCII, e em outras, numa
sequência que começa pelo caractere ‘0’ até o caractere ‘9’. As strings em
Python são formadas por conjuntos de caracteres que podem ser tratadas
também como valores numéricos. Com base nestas afirmações desenvolva
um programa em Python que:
○ Imprima na tela, utilizando print, cada um dos caracteres numéricos e
seu correspondente código numérico. Pesquise como modificar o
comportamento do print para imprimir como caractere e como
número.
'''

# Imprime cada caractere numérico e seu código numérico

for i in range(10):
    caractere = chr(ord('0') + i)
    codigo_numerico = ord(caractere)

    # Imprimir como caractere e número
    print(f"'{caractere}' - {codigo_numerico}")

    # Imprimir apenas o número
    # print(codigo_numerico)
    
    
#ATIVDADE 3.2
'''Modifique o exercício anterior para que a saída imprima também o
código numérico em octal e em hexadecimal.
'''

# Imprime cada caractere numérico, seu código numérico, código octal e código hexadecimal

for i in range(10):
    caractere = chr(ord('0') + i)
    codigo_numerico = ord(caractere)
    codigo_octal = oct(codigo_numerico)
    codigo_hexadecimal = hex(codigo_numerico)

    print(f"'{caractere}' - {codigo_numerico} - Octal: {codigo_octal} - Hexadecimal: {codigo_hexadecimal}")
    
#ATIVDADE 3.3
'''Acrescente ao código do exercício anterior a possibilidade de ler um
caractere qualquer e imprima no mesmo formato do inciso anterior.
Pesquise como ler um valor da entrada padrão.
'''

# Lê um caractere da entrada padrão e imprime suas representações numéricas, octal e hexadecimal

# Solicita ao usuário que insira um caractere
caractere = input("Digite um caractere: ")

# Obtém o código numérico, octal e hexadecimal do caractere
codigo_numerico = ord(caractere)
codigo_octal = oct(codigo_numerico)
codigo_hexadecimal = hex(codigo_numerico)

# Imprime as representações
print(f"'{caractere}' - {codigo_numerico} - Octal: {codigo_octal} - Hexadecimal: {codigo_hexadecimal}")

#ATIVIDADE 3.4

'''Pesquise como trabalha Python os caracteres especiais, ‘ç’ e ‘ã’
por exemplo. Acrescente no código do exercício anterior um exemplo
que demonstra como usar este recurso.'''

# Lê um caractere da entrada padrão e imprime suas representações numéricas, octal e hexadecimal

# Solicita ao usuário que insira um caractere
caractere = input("Digite um caractere: ")

# Obtém o código numérico, octal e hexadecimal do caractere
codigo_numerico = ord(caractere)
codigo_octal = oct(codigo_numerico)
codigo_hexadecimal = hex(codigo_numerico)

# Imprime as representações
print(f"'{caractere}' - {codigo_numerico} - Octal: {codigo_octal} - Hexadecimal: {codigo_hexadecimal}")

# Exemplo com caracteres especiais
caractere_especial1 = 'ç'
caractere_especial2 = 'ã'

codigo_numerico_especial1 = ord(caractere_especial1)
codigo_octal_especial1 = oct(codigo_numerico_especial1)
codigo_hexadecimal_especial1 = hex(codigo_numerico_especial1)

codigo_numerico_especial2 = ord(caractere_especial2)
codigo_octal_especial2 = oct(codigo_numerico_especial2)
codigo_hexadecimal_especial2 = hex(codigo_numerico_especial2)

# Imprime as representações dos caracteres especiais
print(f"'{caractere_especial1}' - {codigo_numerico_especial1} - Octal: {codigo_octal_especial1} - Hexadecimal: {codigo_hexadecimal_especial1}")
print(f"'{caractere_especial2}' - {codigo_numerico_especial2} - Octal: {codigo_octal_especial2} - Hexadecimal: {codigo_hexadecimal_especial2}")


    