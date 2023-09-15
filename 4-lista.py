# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 08/09/2023
# Data de modificação: 15/09/2023
# Versão: 1.2


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

Listas são mutáveis: O seu valor pode mudar constantemente.
Toda lista se inicia com um par de colchetes '[]', e seu conteúdo é definido
como elemento.
"""
berserk = ['Guts', 'Griffith', 'Casca']
lista_sortida = [1, 2.5, 'Nome', True]
print(f"Lista: {berserk}")
print(f"Lista sortida: {lista_sortida}")
print(f"Tipo: {type(berserk)}")
print(f"Tipo: {type(lista_sortida)}")

# Lista numerada.
print(f"Posição de cada elemento: {list(enumerate(berserk))}")
print(f"Escolhendo o segundo elemento: {berserk[1]}")  

# Comprimento/tamanho.
print("Tamanho da lista:", len(berserk), "\n")


# MÉTODOS

# Adiona um elemento (por vez) ao final.
berserk.append('Pippin')
print(f"Adicionando elemento: {berserk}")

# Inserindo um elemento, escolhendo a posição.
berserk.insert(3, 'Judeau')
berserk.insert(4, 'Rickert')
print(f"Inserindo elementos na posição 4 e 5: {berserk}")

# Concatena os elementos da segunda lista ao final da primeira.
# Opcionalmente pode utilizar: lista3 = lista1 + lista2
berserk.extend(['Corkus', 'Gaston'])
print(f"Lista extendida: {berserk}")

# Copia uma lista específica.
berserk_copia = berserk.copy()

# Ordem alfabética dos elementos.
berserk.sort()
print(f"Lista ordenada: {berserk}")

# Inverte a posição dos elementos.
berserk.reverse()
print(f"Lista invertida: {berserk}")

# Remove um elemento, informando a posição específica.
# Caso não seja informado o indiçe, remove o último elemento.
berserk.pop(6)
print(f"Removendo o elemento da posição 7: {berserk}")

# Remove um elemento, informando o valor.
# OBS: REMOVE APENAS O PRIMEIRO ELEMENTO QUE ELE ENCONTRA.
# CASO A LISTA POSSUA ELEMENTOS IGUAIS, NÃO SERÃO REMOVIDOS.
berserk.remove('Griffith')  
print(f"Removendo elemento por valor: {berserk}", "\n")

# Retorna a posição do valor informado.
print(f"Posição do elemento pesquisado: {berserk.index('Guts')}")

# Conta a quantidade de vezes que um elemento aparece.
print(f"Número de vezes que o elemento aparece: {berserk.count('Guts')}")

# Testa se o valor existe.
print(f"O valor informado se enconta na lista?: {'Guts' in berserk}", "\n")

# Removendo todos os elementos.
berserk.clear()
print(f"Removendo... {berserk}", "\n")


# CONVERTENDO UMA LISTA EM UMA STRING

lista = ['Convertendo', 'o', 'conteúdo', 'de', 'uma', 'lista']
print(f"Lista: {lista}")
# Colocando espaços (separador) entre os elementos, e transformando em 
# uma string, utilizando o método '.join'.
juntar = ' '.join(lista)
print(f"String única: {juntar}", "\n")


# UTILIZANDO LOOPS

print("Imprimindo com for:")
for var_temp in range(len(berserk_copia)):
    print(f"{var_temp}: {berserk_copia[var_temp]}")

contador = 0
print("\nImprimindo com while:")
while contador < len(berserk_copia):
    print(f"{contador}: {berserk_copia[contador]}")
    contador += 1


"""
Referências:
https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
https://docs.python.org/3/c-api/list.html?highligh#list-objects
https://docs.python.org/3/library/functions.html?highlight=enumerate#enumerate
https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join
https://www.w3schools.com/python/python_lists.asp
https://www.w3schools.com/python/python_lists_methods.asp
https://www.w3schools.com/python/ref_func_enumerate.asp
https://www.w3schools.com/python/ref_string_join.asp
"""

