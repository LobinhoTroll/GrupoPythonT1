caractere_especial = input("Digite um caractere especial (ex: ç, ã): ")

print(f'\'{caractere_especial}\' - Decimal: {ord(caractere_especial)}, Octal: {oct(ord(caractere_especial))}, Hexadecimal: {hex(ord(caractere_especial))}')
