"""Operadores Aritméticos e Aritméticos Compostos em Python:
Em Python, os operadores aritméticos são semelhantes aos de C/C++, mas há algumas diferenças notáveis. 
Vamos explorar os operadores básicos:"""

# Operadores Aritméticos
a = 10
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
potencia = a ** b

# Operadores Aritméticos Compostos
a += 1  # Equivalente a a = a + 1
b *= 2  # Equivalente a b = b * 2


""" Diferenças principais em relação a C/C++: 
Divisão: Em Python, a divisão padrão (/) retorna um número de ponto flutuante, mesmo se os operandos forem inteiros. Em C/C++,
a divisão de inteiros retorna um inteiro, truncando a parte decimal.

Potência: O operador ** em Python é usado para calcular potências, enquanto em C/C++, você normalmente usaria uma função como ''pow()''.

Representação de Números Inteiros Grandes:
Python não tem limites rígidos para o tamanho dos números inteiros. Pode-se representar números inteiros muito grandes sem se preocupar com overflow. 
Vamos calcular o fatorial de 30:"""

import math

fatorial_30 = math.factorial(30)
print(f"Fatorial de 30: {fatorial_30}")

"""Em C/C++, o maior valor que um inteiro pode representar depende do sistema, mas geralmente é limitado a 2^31 - 1 ou 2^63 - 1
(para inteiros de 32 e 64 bits, respectivamente)."""

""" Imutabilidade de Variáveis Numéricas:
Variáveis numéricas em Python são imutáveis, o que significa que seus valores não podem ser alterados depois de serem atribuídos."""

a = 5
# A próxima linha resultaria em um erro
# a += 1

""" Quando você faz a += 1, na verdade está criando uma nova variável que contém o resultado da operação."""

"""Métodos Disponíveis para Variáveis Inteiras:
Variáveis inteiras em Python não possuem muitos métodos próprios, pois são tipos de dados simples. Alguns métodos úteis incluem:
bit_length(): Retorna o número mínimo de bits necessários para representar o número (excluindo o sinal e zeros à esquerda).
Exemplo: """

num = 42
print(num.bit_length())  # Saída: 6


