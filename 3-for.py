#!/usr/bin/env python
# Autor: João Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 28/10/2022
# Data de modificação:
# Versão: 1.0
# Uso: python3 3-for.py

# ESTRUTURA DE REPETIÇÃO: for

# A estrutura do código segue a PEP8.
# https://peps.python.org/pep-0008/

# Documentação consultada:
# https://docs.python.org/3/reference/compound_stmts.html#the-for-statement

# O padrão de nomeamento de variáveis que o python segue é chamado
# snakecase: nome_da_variavel = 123.

# ESTRUTURA DE REPETIÇÃO: for
# O for é um tipo especial de loop feito para percorrer elementos de uma lista.

# for (variável_temporária) in (lista):
# instruções...

# O for se repete uma vez para cada elemento da lista.
# A cada repetição, a variável temporária assume o valor de um elemento
# da lista, na ordem da lista.

lista = [5, 4, 3, 2, 1]
for elemento in lista:
    print("Valor do elemento da lista é:", elemento)
print()

nomes_cidades = ["Recife", "Olinda", "Jaboatão dos Guararapes", "Paulista"]
for nome in nomes_cidades:
    print(nome)
print()


# UTILIZANDO A FUNÇÃO RANGE

# Documentação consultada:
# https://docs.python.org/3/library/stdtypes.html#ranges

# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será em 1.
for numero in range(10):  # "range" significa faixa.
    print(numero)
    # Este exemplo imprime os números de 0 a 9.
print()

# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.
for numero in range(1, 11):
    print(numero)
    # Este exemplo imprime os números de 1 a 10.
print()

# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1, 20, 2):
    print(numero)
    # Este exemplo imprime os ímpares positivos menores do que 20.
    # Ele começa a valer 1 e salta (passo) a cada 2 até atingir ou passar 20.
print()

# O incremento pode ser também um decremento (incremento negativo).
for numero in range(10, 0, -1):
    print(numero)
# Imprimindo os números de 1 a 10 em ordem decrescente.
print()


# UTILIZANDO UM DICIONÁRIO

# Documentação consultada:
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

# Os dicionários são coleções de itens e os seus elementos são armazenados
# de forma não ordenada.
linux = {
    "criador": "Linux Torvalds",
    "ano": "1991/09/17",
    "base": "UNIX",
    "filosofia": "GNU",
    "interpretador": "Bash",
}
for chave in linux:
    print(f"{chave}: {linux[chave]}")
