# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 27/09/2023
# Data de modificação:
# Versão: 1.0


"""
Dicas:
Utilize quatro espaços em branco para indentação!
Termine uma instrução sempre com uma nova linha!

Referências:
https://peps.python.org/pep-0008/
https://wiki.python.org.br/GuiaDeEstilo
"""


# ESTRUTURAS DE DADOS: set

"""
Um conjunto é uma coleção de valores únicos, utilizado para armazenar múltiplos
elementos em um objeto.
Os conjuntos (chamados de 'Set') não possuem valores duplicados, ordenados e não
são indexados.
Os elementos podem ser de qualquer tipo de dado.
Conjuntos são representados por chaves '{}'.

A diferença entre Conjuntos e Dicionários, em Python, são:
    - Um dicionário possui chave e valor;
    - Um conjunto possui apenas valor.
"""

# Conjunto (set) com tipos de dados diferentes
mix = {'Palavra', 2023, 20.23, True}
print(type(mix))
print(mix, "\n")

# Conjunto com valores repetidos
numeros_inteiros = {0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5}

# Todos os valores repetidos foram ignorados
print(numeros_inteiros, "\n")

# Criando uma lista
numeros_reais_lista = [1.2, 1.2, 2.1, 2.1, 3.2, 3.2, 4.3, 4.3, 5.4, 5.4]
print(numeros_reais_lista)

# Convertendo para conjunto
print(set(numeros_reais_lista), "\n")

# Criando uma tupla
vogais_tupla = ('a', 'a', 'e', 'e', 'i', 'i', 'o', 'o', 'u', 'u')
print(vogais_tupla)

# Convertendo para conjunto. Os elementos do conjunto mudam de ordem a cada acesso.

print(set(vogais_tupla), "\n")

# Adicionando elemetos
cjt = {'b' ,'c', 'd', 'g', 'h'}
cjt.add('JPL')
print(cjt)

# Removendo elementos
cjt.remove('JPL')
print(cjt, "\n")

"""
O método 'union()' realiza a união de todos os conjuntos (separados por vírgula),
em um conjunto especificado.
"""
hdw0 = {'PlacaMae', 'CPU', 'HDD'}
hdw1 = {'MemoriaRam', 'HDD', 'PlacaMae'}
hdw2 = {'FonteDeAlimentacao', 'Gabinete', 'CPU'}
pc = hdw0.union(hdw1, hdw2)
print(pc)


"""
Referências:
https://docs.python.org/3/library/stdtypes.html?highlight=set#set-types-set-frozenset
https://www.w3schools.com/python/python_sets.asp
https://www.w3schools.com/python/ref_set_union.asp
"""

