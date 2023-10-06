# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 20/09/2023
# Data de modificação: 04/10/2023
# Versão: 1.3


"""
Dicas:
Utilize quatro espaços em branco para indentação!
Termine uma instrução sempre com uma nova linha!

Referências:
https://peps.python.org/pep-0008/
https://wiki.python.org.br/GuiaDeEstilo
"""


# ESTRUTURAS DE DADOS: dict

"""
Um dicionário são objetos mapeados que armazena um par de chave/valor, separados por dois pontos 'chave': 'valor'.
Dicionários são representados por chaves '{}'.
A chave e o valor podem ser de qualquer tipo de dado.
Esses objetos são armazenados de forma não ordenada/sequencial.
"""

# Criando um dicionário
linux = {
    'Kernel': 'Linux',
    'Criador': 'Linus Torvalds',
    'Ano': '1991/08/25',
    'Base': 'MINIX',
    'Filosofia': 'GNU',
    'Interpretador': 'Bash',
}

print(linux)
print("\n", type(linux), "\n")

# Acessando apenas as chaves
for chave in linux.keys():
    print(chave)
    
print("\n>>>\n")

# Acessando apenas os valores
for valor in linux.values():
    print(valor)

print("\n>>>\n")

# Acessando ambos
for ambos in linux:
    print(f"{ambos}: {linux[ambos]}")


# Apesar de os dicionários não serem indexados, podemos consultar utilizando colchetes '[]'.
print(f"\n{linux['Kernel']}: {linux['Interpretador']}")


# Utilizando o método get()

"""
O método 'get()' retorna o valor de uma chave especifica. Caso não encontre a chave informada, é retornado um valor
do tipo 'None' que, em Python, é SEMPRE considerado como False.
"""
print(f"\nValor: {linux.get('Base')}")
print(f"Valor: {linux.get('NaoTemChave')}\n")

# Adicionando elemento
linux['Mascote'] = 'Tux'

# Atualizando elemento
linux.update({'Criador': 'Linus Benedict Torvalds'})
print(linux)

# Dicionários NÂO podem ter chaves repetidas. Isso irá sobreescrever o valor da chave existente.
linux['Ano'] = '25/08/1991'
print(linux, "\n")


# Utilizando o método fromkeys()

"""
O método fromkeys() retorna um dicionário com chaves diversas e um valor padrão.
"""
atacado = {}.fromkeys(['Acucar', 'Arroz', 'Feijao', 'Macarrao'], 5.90)
print(atacado)


# Os números precisam ser inteiros ou reais
numero = {'Tres': 3, 'Seis': 6, 'Nove': 9}

print(f"\nSoma: {sum(numero.values())}")
print(f"Menor: {min(numero.values())}")
print(f"Maior: {max(numero.values())}")


"""
Referências:
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
https://docs.python.org/3/library/stdtypes.html?highlight=fromkeys#dict.fromkeys
https://www.w3schools.com/python/python_dictionaries.asp
https://www.w3schools.com/python/ref_dictionary_get.asp
https://www.w3schools.com/python/ref_dictionary_fromkeys.asp
"""
