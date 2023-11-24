# Operadores Aritméticos e Aritméticos Compostos em Python:

"""Em Python, os operadores aritméticos e aritméticos compostos funcionam com variáveis de ponto flutuante de maneira similar aos inteiros.
Aqui estão alguns exemplos:"""

# Operadores Aritméticos
a = 5.0
b = 2.0

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
potencia = a ** b

# Operadores Aritméticos Compostos
a += 1.0  # Equivalente a a = a + 1.0
b *= 2.0  # Equivalente a b = b * 2.0

# Maior e Menor Potência de 2 Representável:
""" Em Python, a maior potência de 2 que pode ser representada é limitada pelo tamanho do tipo de dado float.
Para descobrir esses limites, você pode usar o módulo 'sys':"""

import sys

print(f"Maior potência de 2 representável: {sys.float_info.max_10_exp}")
print(f"Menor potência de 2 representável: {sys.float_info.min_10_exp}")

# Variáveis Numéricas São Imutáveis:
""" Assim como com os inteiros, variáveis de ponto flutuante são imutáveis em Python. Veja um exemplo: """

a = 3.14
# A próxima linha resultaria em um erro
# a += 1.0

# Métodos Disponíveis para Variáveis de Ponto Flutuante:2
""" Variáveis de ponto flutuante em Python não têm muitos métodos específicos, pois são tipos de dados simples. No entanto, 
você pode usar funções embutidas, como round(), math.ceil(), math.floor(), etc., para operações com números de ponto flutuante."""

import math
num = 3.14159

print(round(num, 2))  # Arredonda para 2 casas decimais
print(math.ceil(num))  # Arredonda para cima
print(math.floor(num))  # Arredonda para baixo



