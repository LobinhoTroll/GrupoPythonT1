def print_char_info(char):
    print(f"Caractere: '{char}'")
    print(f" - Código Numérico: {ord(char)}")
    print(f" - Código Octal: {oct(ord(char))}")
    print(f" - Código Hexadecimal: {hex(ord(char))}")
    print()


# Imprime os caracteres numéricos de 0 a 9 e suas informações
for i in range(10):
    print_char_info(str(i))

# Lê um caractere da entrada padrão e imprime suas informações
user_char = input("Digite um caractere: ")
print_char_info(user_char)

# Exemplos de caracteres especiais
special_chars = ['ç', 'ã']

for char in special_chars:
    print_char_info(char)
