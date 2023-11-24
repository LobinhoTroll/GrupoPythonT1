##ATIVIDADE5
''' Durante a aula foi apresentado o tipo de dado que permite representar um
subconjunto dos números de ponto flutuante. Sobre estes tipos de dados:
○ Demonstre como funcionam os operadores aritméticos e aritméticos
compostos em Python;
○ Utilizando o operador de exponenciação mostre qual a maior e a
menor potência de 2 que pode ser representada com variáveis de
ponto flutuante.
○ As variáveis numéricas são imutáveis. Demonstre com exemplos as
implicações desta afirmação;
○ Verifique quais métodos estão disponíveis para as variáveis de ponto
flutuante;
'''

# Operadores Aritméticos e Compostos em float
a = 5.0
b = 2.0

adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

# Operadores Aritméticos Compostos
a += b
b *= 3

print("Adição:", adicao)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Atribuição com Adição:", a)
print("Atribuição com Multiplicação:", b)
print()

# Maior e Menor Potência de 2 com float
maior_potencia_de_2 = 2.0 ** 1023
menor_potencia_de_2 = 2.0 ** -1022

print("Maior Potência de 2:", maior_potencia_de_2)
print("Menor Potência de 2:", menor_potencia_de_2)
print()

# Variáveis Numéricas Imutáveis
num1 = 10.5
num2 = num1

# Tentativa de modificar o valor
# num1[0] = 5.0  # Isso resultará em um erro

# Tentativa de reatribuir o valor
num1 = 5.0

print("Original:", num1)
print("Cópia:", num2)
print()

# Métodos Disponíveis para float
numero = 3.14159
print("Métodos disponíveis para float:", dir(numero))