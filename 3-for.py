# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 28/10/2022
# Data de modificação: 26/08/2023
# Versão: 1.1


"""
Dicas:
Utilize quatro espaços em branco para indentação!
Termine uma instrução sempre com uma nova linha!

Referências:
https://peps.python.org/pep-0008/
https://wiki.python.org.br/GuiaDeEstilo
"""


# ESTRUTURA DE REPETIÇÃO: for

"""
O 'for' é um loop utilizado para percorrer elementos de uma lista.
Ele se repete uma vez, utilizando uma variável temporária, para cada 
elemento da lista.
A cada repetição, a variável temporária assume o valor de um elemento da lista,
de forma sequencial.
"""

lista = [0, 1, 2, 3, 4, 5]
for var_temp in lista:
    print(f"Valor do elemento da lista é: {var_temp}")
print()

cidades = ["Recife", "Olinda", "Jaboatão dos Guararapes", "Paulista"]
for var_temp in cidades:
    print(f"{var_temp}")
print()


# Utilizando intervalos - range

"""
A função 'range()' possibilita criar uma sequência de números (inteiros), 
que varia de um ponto de partida até um ponto final.
O incremento padrão é de 1 a cada iteração do comando 'for'.
O exemplo a seguir imprime os números de 0 a 9:
"""
for numero in range(10):
    print(f"número: {numero}")
print()

"""
Com dois parâmetros, o primeiro será o valor inicial (inclusivo) e o
segundo será o final (exclusivo).
O incremento continuará sendo 1.
O exemplo a seguir imprime os números de 1 a 10:
"""
for numero in range(1, 11):
    print(f"número: {numero}")
print()

"""
Com trẽs parâmetros, o terceiro será interpretado como incremento.
No exemplo, será impresso os números pares menores que 20.
Ele começa a valer 0 e salta (passo) a cada 2 até atingir ou passar 22.
"""
for numero in range(0, 22, 2):
    print(f"número: {numero}")
print()

"""
O incremento pode ser também um decremento (incremento negativo).
O exemplo a seguir imprime os números de 1 a 10 em ordem decrescente:
"""
for numero in range(10, 0, -1):
    print(f"número: {numero}")
print()


print(">>>Tabuada<<<")
multiplicando = int(input("Qual número deseja saber a tabuada: "))
for multplicador in range(1, 11):  # Multiplicando de 1 até 10
    print(f"{multiplicando} X {multplicador} = {multplicador * multiplicando}")
print()


# Utilizando dicionário - dict

"""
Um dicionário são objetos mapeados que armazena um par de chave e valor.
Esses objetos são armazenados de forma não ordenada/sequencial.
"""

print(">>>Dicionário do Linux<<<")
linux = {
    "Kernel": "Linux",
    "Criador": "Linus Torvalds",
    "Ano": "1991/08/25",
    "Base": "MINIX",
    "Filosofia": "GNU",
    "Interpretador": "Bash",
}
for var_temp in linux:
    print(f"{var_temp}: {linux[var_temp]}")



"""
Referências:
https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
https://docs.python.org/3/glossary.html#term-iterator
https://docs.python.org/3/library/stdtypes.html#ranges
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
https://www.w3schools.com/python/python_for_loops.asp
https://www.w3schools.com/python/python_dictionaries.asp
"""
