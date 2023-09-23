# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 15/09/2023
# Data de modificação: 23/09/2023
# Versão: 1.1


"""
Dicas:
Utilize quatro espaços em branco para indentação!
Termine uma instrução sempre com uma nova linha!

Referências:
https://peps.python.org/pep-0008/
https://wiki.python.org.br/GuiaDeEstilo
"""


# ESTRUTURAS DE DADOS: tuple

"""
As tuplas são representadas por parênteses '()' e os seus elementos
sepadados por vírgulas.
Tuplas são imutáveis: o seu valor não muda.
Utilize tuplas quando tiver a certeza de que os elementos não 
necessitam ser alterados.
"""

yuyu_hakusho = ('Yusuke', 'Kuwabara', 'Kurama', 'Hiei')
yuyu_hakusho_sem_parenteses = 'Yusuke', 'Kuwabara', 'Kurama', 'Hiei'
print(yuyu_hakusho)
print(yuyu_hakusho_sem_parenteses, "\n")
print(type(yuyu_hakusho))
print(type(yuyu_hakusho_sem_parenteses), "\n")

# Convertendo lista para tupla.
yh_lista = ['Genkai', 'Keiko', 'Botan', 'Yukina']
print(yh_lista)
print(tuple(yh_lista), "\n")

# Tupla errada.
tupla_nao = 'Toguro'
# Tupla correta. Adicionando uma virtula.
tupla_sim = ('Toguro',)
print(type(tupla_nao))
print(type(tupla_sim), "\n")

"""
O procedimento a seguir apresentará um erro do tipo: AttributeError.
Elementos não podem ser adicionados em uma tupla.
"""
yuyu_hakusho.append('Sensui')
print(yuyu_hakusho, "\n")


"""
Referências:
https://docs.python.org/3/library/stdtypes.html?highlight#tuples
https://www.w3schools.com/python/python_tuples.asp
"""
