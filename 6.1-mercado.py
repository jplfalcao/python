# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 22/09/2023
# Data de modificação: 23/09/2023
# Versão: 1.1


"""
Importa a classe ChainMap do módulo collections. 
A classe ChainMap permite combinar vários dicionários em um único dicionário.
"""
from collections import ChainMap

# Criando três dicionários
mercearia = {'feijao': 7.90, 'arroz': 4.90, 'macarrao': 3.90, 'acucar': 3.90}
frios = {'manteiga': 9.90, 'margarina': 5.90, 'leite': 6.90, 'queijo': 29.90}
limpeza = {'sabonete': 1.90, 'amaciante': 11.90, 'desinfetante': 8.90, 'detergente': 2.90}

"""
Combina os três dicionários em um único dicionário 'produtos', usando ChainMap,
permitindo a pesquisa em todos os dicionários de uma vez.
"""
produtos = ChainMap(mercearia, frios, limpeza)

"""
Utilizando o método 'lower()', a pequisa será realizada, mesmo se o utilizador 
digitar letras minúsculas e/ou maiúsculas (case insensitive).
"""
consulta = input("Qual produto deseja pesquisar: ").lower()

"""
Realiza o teste, utilizando o método 'get()', se o resultado de
'consulta', no dicionário 'produtos', não é 'is not' None.
"""
if produtos.get(consulta) is not None:
    print(f"O valor de {consulta} é: R${produtos[consulta]:.2f}")
else:
    print(f'O produto solicitado não consta no mercado.')


"""
Referências:
https://docs.python.org/3/library/collections.html?highlight=chainmap#chainmap-objects
https://www.geeksforgeeks.org/chainmap-in-python/
"""
