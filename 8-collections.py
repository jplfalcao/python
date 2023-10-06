# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 04/10/2023
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

# MÓDULO COLLECTIONS

"""
O módulo 'collections' é uma biblioteca que fornece tipos de dados de contêineres.
Um Container é um objeto usado para armazenar diferentes objetos como, listas, dicionários, conjuntos, e tuplas.
"""

# Objeto Counter

"""
O 'Counter' é uma subclasse do dicionário ('dict'). Ele recebe um iterável como parâmetro
e cria um objeto, contendo como chave o elemento da lista, passado como parâmetro, e como
valor a quantidade de ocorrências desse elemento.

É muito útil para contar a frequência de elementos em uma lista.
"""

# Importa a classe Counter do módulo collections
from collections import Counter

frutas = Counter(['maça', 'banana', 'laranja', 'maça', 'uva', 'banana', 'maça', 'uva', 'banana', 'maça'])

print(frutas)
print(type(frutas), "\n")


# Objeto OrderedDict

"""
O 'OrderedDict' é uma subclasse do dicionário ('dict'), que "lembra" a ordem em que as chaves foram inseridas.
O dicionário sempre será ordenado, mesmo que as chaves sejam adicionadas ou removidas.
"""

# Importa a classe OrderedDict do módulo collection
from collections import OrderedDict

verduras = OrderedDict({'coentro': 1.90, 'cenoura': 2.90, 'tomate': 3.90, 'batata': 4.90, 'cebola': 5.90})

print(verduras)
print(type(verduras), "\n")

# Testando a ordem dos elementos com 'dict'
dicio1 = {'alho': 9.90, 'sal': 2.90}
dicio2 = {'sal': 2.90, 'alho': 9.90}

print(dicio1 == dicio2)

# Testando a ordem dos elementos com 'OrderedDict'
order1 = OrderedDict({'alho': 9.90, 'sal': 2.90})
order2 = OrderedDict({'sal': 2.90, 'alho': 9.90})

print(order1 == order2, "\n")


# Objeto defaultdict

"""
O 'defaultdict' é uma subclasse do dicionário ('dict'), que fornece um valor padrão para chaves "que não existem".
Podemos garantir que um valor sempre esteja disponível, mesmo que a chave não exista.
"""

# Importa a classe defaultdict do módulo collections
from collections import defaultdict

# O valor padrão 'list' atribui uma lista a chaves que não existam.
tempero = defaultdict(list)

# Adicionando elementos a lista 'feijao'
tempero['feijao'].append('acafrao')
tempero['feijao'].append('cominho')

print(tempero['feijao'])

# Como a chave 'oregano' não existe, uma lista vazia é criada, como valor padrão.
print(tempero['oregano'])
print(type(tempero), "\n")


# Objeto namedtuple

"""
O 'namedtuple' é uma subclasse da 'tuple', que permite definir nomes para seus elementos.
É útil para criar tipos de dados imutáveis, com nomes significativos.
"""

# Importa a classe namedtuple do módulo collections
from collections import namedtuple

# Declarando uma 'namedtuple', chamada 'ingredientes', com seis parâmetros.
ingredientes = namedtuple('ingredientes', ['trigo', 'ovos', 'leite', 'acucar', 'margarina', 'fermento'])

# Atribuindo valores aos parâmetros
bolo = ingredientes(trigo='3 xícaras', ovos=3, leite='1 e 1/2 xícara', acucar='2 xícaras', margarina='4 colheres', fermento='1 colher')

print(bolo)
print(type(bolo), "\n")


# Objeto deque

"""
O 'deque' é uma subclasse da 'list', que permite acessar os elementos de uma lista, de forma dinámica.
"""

# Importa a classe deque do módulo collections
from collections import deque

# Criando um 'deque'
churrasco = deque(['linguica', 'frango', 'farofa', 'vinagrete'])
print(type(churrasco))
print(churrasco)
# Adicionando um elemento a esquerda
churrasco.appendleft('carne')
print(churrasco)
churrasco.appendleft('peixe')
print(churrasco)
# Removendo um elemento a esquerda
churrasco.popleft()
print(churrasco, "\n")


# Objeto ChainMap

"""
O 'ChainMap' é uma subclasse do dicionário ('dict'), que permite combinar vários dicionários em um único dicionário.
"""

# Importa a classe ChainMap do módulo collections
from collections import ChainMap

# Criando três dicionários
mercearia = {'feijao': 7.90, 'arroz': 4.90, 'macarrao': 3.90, 'acucar': 3.90}
frios = {'manteiga': 9.90, 'margarina': 5.90, 'leite': 6.90, 'queijo': 29.90}
limpeza = {'sabonete': 1.90, 'amaciante': 11.90, 'desinfetante': 8.90, 'detergente': 2.90}

# Combina os três dicionários em um único dicionário 'produtos', permitindo a pesquisa em todos os dicionários.
produtos = ChainMap(mercearia, frios, limpeza)

# Utilizando o método 'lower()', a pequisa será realizada, mesmo se for digitado letras minúsculas e/ou maiúsculas
# (case insensitive).

print("\t\t>>>MERCADO<<<")
consulta = input("Qual produto deseja pesquisar: ").lower()

# Testa, utilizando o método 'get()', se o resultado de 'consulta', no dicionário 'produtos', não é ('is not') 'None'.
if produtos.get(consulta) is not None:
	print(f"O valor de {consulta} é: R${produtos[consulta]:.2f}")
else:
	print(f'O produto solicitado não consta no mercado.')


"""
Referências:
https://docs.python.org/3/library/collections.html#module-collections
https://www.geeksforgeeks.org/python-collections-module/
https://acervolima.com/modulo-de-colecoes-python/
"""
