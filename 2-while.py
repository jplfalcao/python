#!/usr/bin/env python
# Autor: João Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 28/10/2022
# Data de modificação:
# Versão: 1.0
# Uso: python3 2-while.py

# ESTRUTURA DE REPETIÇÃO: while

# A estrutura do código segue a PEP8.
# https://peps.python.org/pep-0008/

# Documentação consultada:
# https://docs.python.org/3/reference/compound_stmts.html#while

# O padrão de nomeamento de variáveis que o python segue é chamado
# snakecase: nome_da_variavel = 123.

import time  # Importando o módulo "time".

inicio = 0
fim = 10
while inicio <= fim:  # Definimos o número de repetições
    # (O contador chegará até o valor da variável "fim").
    inicio += 1  # Variável contadora que será incrementada até chegar
    # ao número que foi definido.
    print("Número:", inicio)
    time.sleep(1)  # "Sleep" é um método do módulo "time".
    if inicio == 5:
        print("Paramos a contagem por aqui!\n")
        break  # O comando "break" sai imediatamente do laço de repetição.

senha = input("Digite sua senha: ")

while senha != "abc123":
    senha = input("Senha inválida! Tente novamente: ")
print("\nAcesso permitido!")
