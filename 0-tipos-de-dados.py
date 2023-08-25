# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 29/10/2022
# Data de modificação: 15/08/2023
# Versão: 1.1


"""
Dicas:
Utilize quatro espaços em branco para indentação!
Termine uma instrução sempre com uma nova linha!

Referências:
https://peps.python.org/pep-0008/
https://wiki.python.org.br/GuiaDeEstilo
"""


# TIPOS DE DADOS

# STRING

# Uma String, em Python, é uma sequência de caracteres.

# Um dado é considerado do tipo string, sempre que:
# 0) Estiver entre àspas simples -> 'python', '2023', 'True'
# 1) Estiver entre àspas duplas -> "python", "2023", "True"
# 2) Estiver entre àspas simples triplas -> '''python''', '''2023''', '''True'''
# 3) Estiver entre àspas duplas triplas -> """python""", """2023""", """True"""

# O operador '=' é um operador de atribuição, que significa: "recebe".

nome0 = 'Python'

"""
A função 'print()' exibe os argumentos informados na saída padrão.
A função 'type()' é utilizada para determinar o tipo de dado (objeto).
"""

print(nome0)
print((type(nome0)))

nome1 = "2023"
print(nome1)
print((type(nome1)))

nome2 = """True"""
print(nome2)
print((type(nome2)), """\n""")


# Slice de string

nome3 = "python language"

# Posição dos caracteres
# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14 ]
# ["p", "y", "t", "h", "o", "n", " ", "l", "a", "n", "g", "u", "a", "g", "e"]

print(nome3[0:2])
print(nome3[0:6])
print(nome3[7:15])


# Comprimento de uma string

# A função 'len()' apresenta o tamanho (números de itens) de um objeto.

print(len(nome3))


# Split de string

# Separa as palavras

# [   0       1   ]
# "pyhton language"

print(nome3.split()[0])
print(nome3.split()[1], "\n")


# Alterando/modificando strings

nome4 = "pYtHoN lAnGuAgE"
print(nome4.lower())  # Todas as letras minúsculas
print(nome4.upper())  # Todas as letras maiúsculas
print(nome4.title())  # Letras iniciais de cada palavra maiúsculas
print(nome4.replace("E", ">I<"), "\n")  # Troca uma srting por outra


# NUMÉRICO

a = 37
b = 13.5
print(a, type(a))
print(b, type(b), "\n")


# OPERADORES ARITMÉTICOS

print(2 + 1)
print(4 - 3)
print(7 * 6)
print(10 / 5)
print(17 // 3)  # Divisão inteira
print(5 ** 5)  # Exponenciação (Potência)
print(37 % 36, "\n")  # Resto da divisão (Módulo)


# CONVERSÃO DE VARIÁVEIS (Casting)

x = str(17)
y = int(23.5)  # Ao converter valores 'float' para 'int', perdemos precisão.
z = float(x)
print(x, type(x))
print(y, type(y))
print(z, type(z), "\n")


# OPERADORES BOLEANOS

# Os operadores booleanas são declarados, SEMPRE, com a primeira letra maiúscula.

tem_cafe = True
tem_bolacha = False

print(not tem_cafe)

"""
Negação (not): Se um valor booleano for verdadeiro (True), 
o resultado será falso (False) e vice-versa.
"""

print(tem_cafe or tem_bolacha)

"""
OU (or): É uma operação binária que depende de dois valores, 
sendo APENAS falso quando os dois valores estão falsos.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(tem_cafe and tem_bolacha, "\n")

"""
E (and): É uma operação binária que depende de dois valores, 
sendo APENAS verdadeiro quando os dois valores estão verdadeiros.

True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""


# OPERADORES RELACIONAIS

dolar = 1.00
real = 5.00
print(dolar > real)  # Maior que
print(dolar < real)  # Menor que
print(dolar == real)  # Igual
print(dolar >= real)  # Maior ou igual
print(dolar <= real)  # Menor ou igual
print(dolar != real, "\n")  # Diferente

# Os resultados gerados são valores booleanos.


# OUTRAS ATRIBUIÇÕES

# Atribuição dupla

num1, num2 = 20, 23
print(int(num1), int(num2))

i = 5
j = 6

# Incremento

i += 1  # i = i + 1
print(i)

# Decremento

j -= 1  # i = i - 1
print(j)


# ENTRADA DE DADOS

"""
Os dados recebidos através da função 'input()', SEMPRE serão do tipo string(str).
Pode-se utilizar o método de conversão (Casting), convertendo o tipo de dado 
de uma determidada variável.

A função 'input()' vai armazenar o que for digitado, na variável 'nome'.
A função 'input()' vai armazenar o que for digitado, na variável 'idade'.
"""

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))


# PROCESSAMENTO


# SAÍDA DE DADOS E FORMATAÇÃO

"""
1-Exemplo de formatação 'antiga' da função 'print()':
print("%s tem %s anos." % (nome, idade))

2-Exemplo de formatação 'moderna' da função 'print()':
print("{0} tem {1} anos.".format(nome, idade))

3-Uso atual de formatação da função 'print()':
"""
print(f"\n{nome} tem {idade} anos.")
print("\nTipo de dado da varável nome: ", type(nome))
print("Tipo de dado da varável idade: ", type(idade))



"""
Referências:
https://docs.python.org/3/library/stdtypes.html
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/tutorial/inputoutput.html
https://www.w3schools.com/python/python_casting.asp
https://acervolima.com/tipos-de-dados-python/
"""
