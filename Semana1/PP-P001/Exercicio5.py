import sys

a = 10
b = 3

soma = a + b
print("Adição:", soma)

subtracao = a - b
print("Subtração:", subtracao)

multiplicacao = a * b
print("Multiplicação:", multiplicacao)

divisao = a / b
print("Divisão:", divisao)

divisao_inteira = a // b
print("Divisão Inteira:", divisao_inteira)

resto_divisao = a % b
print("Resto da Divisão:", resto_divisao)

exponenciacao = a ** b
print("Exponenciação:", exponenciacao)

x = 5

x += 3  
print("Adição e Atribuição:", x)

x -= 2  
print("Subtração e Atribuição:", x)

x *= 4  
print("Multiplicação e Atribuição:", x)

x /= 2  
print("Divisão e Atribuição:", x)

x //= 3  
print("Divisão Inteira e Atribuição:", x)

x %= 2  
print("Resto da Divisão e Atribuição:", x)

x **= 3  
print("Exponenciação e Atribuição:", x)

menor_potencia_de_2 = 2.0 ** sys.float_info.min_exp
print(f"A menor potência de 2 representável é 2^{sys.float_info.min_exp}: {menor_potencia_de_2}")

maior_potencia_de_2 = 2.0 ** sys.float_info.max_exp
print(f"A maior potência de 2 representável é 2^{sys.float_info.max_exp}: {maior_potencia_de_2}")
#O maior valor em minha máquina deu overflow.

#Imutabilidade respondida na 2.3

#Métodos disponíveis respondida na 2.4
#float = 42
#print(dir(float))

