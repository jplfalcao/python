# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 08/09/2023
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


# ESTRUTURAS DE DADOS: list

"""
As listas são usadas para armazenar coleções de itens em uma única variável.
Elas podem ser:
  - Dinâmicas: não possuindo tamanho fixo;
  - De qualquer tipo: sem tipo de dado específico.
"""

# Toda lista se inicia com um par de colchetes '[]', e o conteúdo é definido como elemento.
lista_sortida = [1, 2.5, "Nome", True]
berserk = ["Guts", "Griffith", "Casca"]
print(f"Lista: {berserk}")
print(f"Tipo: {type(berserk)}")
print(f"Tipo: {type(lista_sortida)}")

# Apresenta a lista numerada.
berserk_numerado = enumerate(berserk)
print(f"Posição de cada elemento: {list(berserk_numerado)}")
print(f"Escolhendo o segundo elemento: {berserk[1]}")  

# Comprimento/tamanho de uma lista.
print("Tamanho da lista:", len(berserk), "\n")


# MÉTODOS DE LISTAS

# O método '.append' adiona um elemento ao final na lista.
berserk.append("Pippin")
print(f"Adicionando elemento: {berserk}")

# Inserindo um elemento na lista, escolhendo a sua posição.
berserk.insert(3, "Judeau")
berserk.insert(4, "Rickert")
print(f"Inserindo elementos na posição 4 e 5: {berserk}")

# Realiza a junção de listas, adicionando (contatenando) os elementos
# da segunda lista ao final da primeira.
berserk_extendido = ["Corkus",	"Gaston"]
berserk.extend(berserk_extendido)
print(f"Lista extendida: {berserk}")

# Cópia uma lista específica.
berserk_copia = berserk.copy()
print(f"Copiando uma lista: {berserk}")

# Ordena uma lista, em ordem alfabética.
berserk.sort()
print(f"Lista ordenada: {berserk}")

# Inverte a posição dos elementos da lista.
berserk.reverse()
print(f"Lista invertida: {berserk}")

# Remove um elemento da lista, informando a posição específica.
berserk.pop(6)
print(f"Removendo o elemento da posição 7: {berserk}")

# Remove um elemento da lista, informando o valor. OBS: REMOVE APENAS O PRIMEIRO ELEMENTO
# QUE ELE ENCONTRA. CASO A LISTA POSSUA ELEMENTOS IGUAIS, NÃO SERÃO REMOVIDOS.
berserk.remove("Griffith")  
print(f"Removendo elemento escolhendo seu valor: {berserk}", "\n")

# O Retorna a posição na primeira ocorrência do valor especificado.
test_index = berserk.index('Guts')
print(f"Posição do elemento pesquisado: {test_index}")

# Conta a quantidade de vezes que um elemento aparece em uma lista.
print(f"Número de vezes que o elemento aparece: {berserk.count('Guts')}")

# Navega pela lista testando o seu valor.
print(f"O valor informado se enconta na lista?: {'Guts' in berserk}")


"""
Referências:
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
https://docs.python.org/3/c-api/list.html?highligh#list-objects
https://docs.python.org/3/library/functions.html?highlight=enumerate#enumerate
https://www.w3schools.com/python/python_lists.asp
https://www.w3schools.com/python/python_lists_methods.asp
https://www.w3schools.com/python/ref_func_enumerate.asp
"""
