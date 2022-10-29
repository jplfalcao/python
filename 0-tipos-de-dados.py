#!/usr/bin/env python
# Autor: João Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 29/10/2022
# Data de modificação:
# Versão: 1.0
# Uso: python3 0-tipos-de-dados.py

# TIPOS DE DADOS

# A estrutura do código segue a PEP8.
# https://peps.python.org/pep-0008/

# Documentação consultada:
# https://docs.python.org/3/library/stdtypes.html

# O padrão de nomeamento de variáveis que o python segue é chamado
# snakecase: nome_da_variavel = 123.

# NUMÉRICO
x = 36
y = 13.5
print(x, type(x))  # Função utilizada para determinar o tipo de dado.
print(y, type(y), '\n')

# OPERADORES ARITMÉTICOS
a = 0 + 1  # Soma
b = 2 - 3  # Subtração
c = 4 * 5  # Multiplicação
d = 6 / 7  # Divisão
e = 8 // 9  # Divisão inteira
f = 10 ** 11  # Potência
g = 12 % 13  # Resto de divisão
print(a, b, c, d, e, f, g, '\n')

# CONVERSÃO DE VARIÁVEIS (Casting)
x = str(17)
y = int(23.5)
z = float(x)
print(x, type(x))
print(y, type(y))
print(z, type(z), '\n')

# OPERADORES BOLEANOS
tem_cafe = True
tem_bolacha = False
print(not tem_cafe)
print(tem_cafe or tem_bolacha)
print(tem_cafe and tem_bolacha, '\n')

dolar = 3.00
real = 1.00
print(dolar > real)  # Maior que
print(dolar < real)  # Menor que
print(dolar == real)  # Igual
print(dolar >= real)  # Maior ou igual
print(dolar <= real)  # Menor ou igual
print(dolar != real)  # Diferente
