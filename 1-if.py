#!/usr/bin/env python
# Autor: João Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 28/10/2022
# Data de modificação:
# Versão: 1.0
# Uso: python3 1-if.py

# ESTRUTURAS CONDICIONAIS: if elif else

# A estrutura do código segue a PEP8.
# https://peps.python.org/pep-0008/

# Documentação consultada:
# https://docs.python.org/3/tutorial/controlflow.html#if-statements

# O padrão de nomeamento de variáveis que o python segue é chamado
# snakecase: nome_da_variavel = 123.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("\nSua média foi:", media)

# Estrutura que será testada.
if media >= 7:
	print("Resultado: Aprovado! :-)")
# Quando o teste do if é negado, é efetuado outro teste com o elif.
elif (media >= 6) and (media <= 6.9):
	print("Resultado: Prova final! :-0")
# Quando nenhuma das condições são satisfeitas, é executado o else.
else:
	print("Resultado: Reprovado! :-(")
