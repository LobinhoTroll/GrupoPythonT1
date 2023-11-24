#ATIVDADE 2.1
'''Demonstre como funcionam os operadores aritméticos e aritméticos
compostos em Python e destaque as principais novidades e diferenças
em relação ao conjunto de operadores com inteiros disponíveis em
C/C++ ;'''

# Operadores Aritméticos Básicos
a = 5
b = 3

adicao = a + b  # Resultado: 8
subtracao = a - b  # Resultado: 2
multiplicacao = a * b  # Resultado: 15
divisao = a / b  # Resultado: 1.6666666666666667 (divisão como ponto flutuante)

# Operadores Aritméticos Compostos
a += b  # Equivalente a: a = a + b (a agora é 8)
a -= b  # Equivalente a: a = a - b (a agora é 5)
a *= b  # Equivalente a: a = a * b (a agora é 15)
a /= b  # Equivalente a: a = a / b (a agora é 5.0)

# Exponenciação
exponenciacao = 2 ** 3  # Resultado: 8

# Impressão dos resultados
print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Exponenciação:", exponenciacao)

#diferenças
#em relação ao conjunto de operadores com inteiros disponíveis em
#C/C++ ;

# Divisão de Inteiros
# Em Python 3, a divisão entre inteiros resulta em ponto flutuante.
# Em C/C++, a divisão de inteiros é truncada para um número inteiro.

# Exemplo em C/C++
# int resultado_c = 5 / 2;  # Resultado: 2 (divisão truncada)

# Exemplo em Python
resultado_python = 5 / 2  # Resultado: 2.5 (divisão como ponto flutuante)

# Exponenciação
# Python possui um operador específico (**), enquanto em C/C++, você usaria a função pow().

# Exemplo em C/C++
# #include <cmath>
# int resultado_c = pow(2, 3);  # Resultado: 8

# Exemplo em Python
resultado_python = 2 ** 3  # Resultado: 8

##ATIVIDADE 2.2
'''Demonstre a possibilidade de representar números inteiros
significativamente grandes calculando o fatorial de 30 e comparando
o resultado com o maior valor inteiro que pode ser representado em
C/C++;'''

import math

# Calcular o fatorial de 30 em Python
fatorial_30 = math.factorial(30)

print("Fatorial de 30 em Python:", fatorial_30)

#ATIVIDADE 2.3
'''As variáveis numéricas são imutáveis. Demonstre com exemplos as
implicações desta afirmação;
'''

# Variáveis numéricas são imutáveis
numero = 5
print("Antes da modificação:", numero)

# Tentativa de modificar o valor
# Isso resultará em um erro
# TypeError: 'int' object does not support item assignment
# número[0] = 2

# Tentativa de reatribuir o valor
# Isso funciona, mas cria uma nova variável com um novo valor
numero = 10
print("Depois da reatribuição:", numero)

# Variáveis numéricas são imutáveis
numero_ponto_flutuante = 3.14
print("Antes da modificação:", numero_ponto_flutuante)

# Tentativa de modificar o valor
# Isso resultará em um erro
# TypeError: 'float' object does not support item assignment
# número_ponto_flutuante[0] = 2

# Tentativa de reatribuir o valor
# Isso funciona, mas cria uma nova variável com um novo valor
numero_ponto_flutuante = 2.718
print("Depois da reatribuição:", numero_ponto_flutuante)

#ATIVDADE 2.4
'''Verifique quais métodos estão disponíveis para as variáveis inteiras;'''

# Métodos disponíveis para variáveis inteiras em Python

# Exemplo 1: bit_length()
numero1 = 42
print("Número:", numero1)
print("Número de bits necessários:", numero1.bit_length())  # Saída: 6
print()

# Exemplo 2: to_bytes() e from_bytes()
numero2 = 255
bytes_representation = numero2.to_bytes(2, byteorder='big')
print("Número:", numero2)
print("Representação em bytes:", bytes_representation)  # Saída: b'\x00\xff'
converted_number = int.from_bytes(bytes_representation, byteorder='big')
print("Convertido de bytes para número:", converted_number)  # Saída: 255
print()

# Exemplo 3: conjugate() para números imaginários
numero_imaginario = 3j
conjugado = numero_imaginario.conjugate()
print("Número imaginário:", numero_imaginario)
print("Conjugado:", conjugado)  # Saída: -3j
print()

# Exemplo 4: real e imag para números complexos
numero_complexo = 2 + 3j
print("Número complexo:", numero_complexo)
print("Parte real:", numero_complexo.real)  # Saída: 2.0
print("Parte imaginária:", numero_complexo.imag)  # Saída: 3.0