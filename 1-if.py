# Autor: João PauLo Falcão
# Github: https://github.com/jplfalcao
# Data de criação: 28/10/2022
# Data de modificação: 23/09/2023
# Versão: 1.2


"""
Dicas:
Utilize quatro espaços em branco para indentação!
Termine uma instrução sempre com uma nova linha!

Referências:
https://peps.python.org/pep-0008/
https://wiki.python.org.br/GuiaDeEstilo
"""

# ESTRUTURA CONDICIONAL

"""
O if (Se), elif (else if | Senão Se), else (Senão), nos permite executar ações
alternativas com base em condições (testes).
"""

print("\n>>>Média Escolar<<<")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nMédia: {media:.2f}")

"""
Condição que será testada com o comando 'if'.
Se for verdadeiro, o bloco de código é executado.
"""
if media >= 7:
    print("Resultado: Aprovado! :-)\n")
# Quando o teste do 'if' é falso, é efetuado outro teste com o comando 'elif'
elif media >= 6 and media < 7:
    print("Resultado: Prova final! :-/\n")
# Quando nenhuma das condições é verdadeira, é executado o comando 'else'
else:
    print("Resultado: Reprovado! :-(\n")

print("\n>>>Índice de Massa Corporal<<<")
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)

print(f"\nIMC: {imc:.2f}")

if imc < 18.50:
    print("Abaixo do peso!\n")
elif imc >= 18.50 and imc <= 24.99:
    print("Peso normal!\n")
elif imc >= 25.00 and imc <= 29.99:
    print("Acima do peso!\n")
else:
    print("Obesidade!\n")


"""
Referências:
https://docs.python.org/3/tutorial/controlflow.html#if-statements
https://docs.python.org/3/reference/compound_stmts.html#the-if-statement
https://www.w3schools.com/python/python_conditions.asp
https://www.geeksforgeeks.org/python-if-else/
https://www.minhavida.com.br/saude/tratamento/3870-imc
"""
