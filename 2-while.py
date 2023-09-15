# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 28/10/2022
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


# ESTRUTURA DE REPETIÇÃO: while

"""
O loop 'while' será repetido enquanto a expressão booleana for verdadeira.
Expressão booleane é toda expressão onde o resultado será verdadeiro (True)
ou falso (False).

IMPORTANTE: O LOOP 'WHILE' PRECISA DE UM CRITÉRIO DE PARADA, PARA NÃO SE TORNAR
UM LOOP INFINITO.

O 'while' testa repetidamente a expressão e, se for verdadeira, 
executa o primeiro conjunto; se a expressão for falsa 
(que pode ser a primeira vez que é testada), o conjunto da cláusula else, 
se presente, é executado e o loop é encerrado.
"""


# Importando o módulo 'time'.
import time

inicio = 0
fim = 10
while inicio < fim:
    print(f"Número: {inicio}")
    # O 'sleep' é um método do módulo 'time', onde foi definido o atraso de 1s.
    time.sleep(1)
    if inicio == 5:
        print("Paramos a contagem por aqui!\n")
        # A instrução 'break' sai imediatamente do laço de repetição.
        break
    # Contador que será incrementado até chegar ao valor da variável 'fim'.
    inicio += 1    


print("\n>>>Login no Sistema<<<")
senha = input("Digite sua senha: ")

while senha != "abc123":
    senha = input("Senha inválida! Tente novamente: ")
print("\nAcesso permitido!")


"""
Referências:
https://docs.python.org/3/reference/compound_stmts.html#while
https://docs.python.org/3/library/time.html?highlight=time#time.sleep
https://www.w3schools.com/python/python_while_loops.asp
"""

