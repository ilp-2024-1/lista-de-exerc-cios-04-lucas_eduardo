# Construa soluções de algoritmos e implemente-os utilizando a linguagem de programação
# Python para os seguintes casos:
# OSBERVAÇÃO:
# Exemplos no pdf da lista;
# As soluções apresentadas NÃO devem usar as funções buit-in das listas em Python;
# As soluções apresentadas NÃO devem usar funções definidas pelo usuário;
# As saídas das soluções devem seguir o formato estabelecido nos exemplos,
# quando demonstrado.

# VETORES (array unidimensional):

# 1. Escreva um programa que leia 10 valores inteiros e armazene em uma lista. O pro-
# grama deve imprimir no terminal quantos valores pares foram digitados pelo usuário.
# Dica: use o operador “%” para verificar se o número é par (ZERO é neutro, ZERO NÃO
# É PAR).

# entrada = input("Dez valores separados por espaço: ")
# lista_entrada = []
# quantidade_pares = 0

# for x in entrada:
#     if x != " ":
#         lista_entrada = lista_entrada + [int(x)]

# for x in lista_entrada:
#     if x % 2 == 0:
#         quantidade_pares = quantidade_pares + 1

# print(f"Quantidade de valores pares: {quantidade_pares}")


# 2. Escreva um programa que recebe como entrada valores inteiros para criar duas listas
# de mesmo tamanho. O tamanho das listas deverá ser definido pelo usuário. O pro-
# grama deverá somar os valores pares e ímpar de cada uma das listas. Em seguida,
# comparar as somas e informar qual dos somatórios é maior ou se há um empate.

# tamanho_listas = int(input("Tamanho fixo para duas listas: "))
# lista1 = []
# lista2 = []
# numero_elemento_lista1 = 1
# numero_elemento_lista2 = 1
# quantidade_pares_lista1 = 0
# quantidade_pares_lista2 = 0
# quantidade_impares_lista1 = 0
# quantidade_impares_lista2 = 0

# for x in range(tamanho_listas):
#     elemento = int(input(f"{numero_elemento_lista1}º valor da primeira lista: "))
#     lista1 += [elemento]
#     numero_elemento_lista1 += 1

# for x in range(tamanho_listas):
#     elemento = int(input(f"{numero_elemento_lista2}º valor da segunda lista: "))
#     lista2 += [elemento]
#     numero_elemento_lista2 += 1

# for x in lista1:
#     if x % 2 == 0:
#         quantidade_pares_lista1 += 1
#     else:
#         quantidade_impares_lista1 += 1

# for x in lista2:
#     if x % 2 == 0:
#         quantidade_pares_lista2 += 1
#     else:
#         quantidade_impares_lista2 += 1

# print(f"Pares na primeira lista = {quantidade_pares_lista1}\nPares na segunda lista = {quantidade_pares_lista2}")

# if quantidade_pares_lista1 > quantidade_pares_lista2:
#     print("listaPar1 > listaPar2")
# elif quantidade_pares_lista1 < quantidade_pares_lista2:
#     print("listaPar1 < listaPar2")
# else:
#     print("listaPar1 = listaPar2")

# print(f"Ímpares na primeira lista = {quantidade_impares_lista1}\nÍmpares na segunda lista = {quantidade_impares_lista2}")

# if quantidade_impares_lista1 > quantidade_impares_lista2:
#     print("listaImpar1 > listaImpar2")
# elif quantidade_impares_lista1 < quantidade_impares_lista2:
#     print("listaImpar1 < listaImpar2")
# else:
#     print("listaImpar1 = listaImpar2")


# 3. leia 10 valores inteiros e armazene em uma lista. O programa deve imprimir no terminal
# quantos valores pares foram digitados pelo usuário. Dica: use o operador “%” para
# verificar se o número é par (ZERO é neutro, ZERO NÃO É PAR).

# entrada = input("Dez valores separados por espaço: ")
# lista_entrada = []
# quantidade_pares = 0

# for x in entrada:
#     if x != " ":
#         lista_entrada = lista_entrada + [int(x)]

# for x in lista_entrada:
#     if x % 2 == 0:
#         quantidade_pares = quantidade_pares + 1

# print(f"Quantidade de valores pares: {quantidade_pares}")

# 4. Escreva um programa que receba como entrada 3 parâmetros: um valor inteiro corres-
# pondente à quantidade de elementos de dois arrays unidimensionais; duas sequências
# de valores do tamanho do primeiro parâmetro, os quais deverão ser armazenados em
# duas listas distintas. Em seguida, o programa deverá criar uma lista resultante formada
# pela intercalação dos valores de cada uma das sequências de entrada. Como saída o
# programa deverá imprimir as duas listas iniciais e a lista resultante.

# quantidade_elementos = int(input("Quantidade de elementos das listas: "))
# lista1 = []
# lista2 = []
# lista3 = []
# numero_elemento_lista1 = 1
# numero_elemento_lista2 = 1

# for x in range(quantidade_elementos):
#     entrada = input(f"{numero_elemento_lista1}º elemento da primeira lista: ")
#     numero_elemento_lista1 += 1
#     lista1 += [entrada]

# for x in range(quantidade_elementos):
#     entrada = input(f"{numero_elemento_lista1}º elemento da segunda lista: ")
#     numero_elemento_lista2 += 1
#     lista2 += [entrada]

# lista3 = lista1[::] + lista2[::]

# print(lista3)

# 5. Escreva um programa que receba como entrada uma sequência de valores inteiros.
# Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores.

# quantidade_valores = int(input("Quantidade de valores à serem analisados: "))
# numero_elemento = 2
# lista_sequencia = []
# media_valores = 0
# soma_valores = 0

# primeiro_valor = int(input("1º elemento da sequência: "))

# menor_valor = primeiro_valor
# maior_valor = primeiro_valor
# soma_valores += primeiro_valor

# for x in range(quantidade_valores-1):
#     elemento = int(input(f"{numero_elemento}º elemento da sequência: "))
#     numero_elemento += 1
#     soma_valores += elemento
    
#     if elemento > maior_valor:
#         maior_valor = elemento
    
#     elif elemento < menor_valor:
#         menor_valor = elemento
    
# print(f"Menor valor: {menor_valor}\nMaior valor: {maior_valor}\nMédia aritmética: {soma_valores/quantidade_valores:.1f}")


# 6. Crie um programa que solicite ao usuário uma lista de números inteiros e uma string
# de mesmo comprimento. O programa deve substituir os números nos índices ímpares
# da lista por caracteres correspondentes da string nos mesmos índices. Exiba a se-
# quência resultante, separada por um espaço em branco.

# entrada1 = input("Lista de números inteiros separados por espaço: ")
# lista_inteiros = []

# for x in entrada1:
#     if x != " ":
#         lista_inteiros += [int(x)]

# string = input("Palavra com a mesma quantidade de caracteres da lista: ")

# if len(string) != len(lista_inteiros):
#     print("A palavra e a lista não possuem a mesma quantidade de caracteres e valores.")

# else:
#     indice = 0
#     lista_final = lista_inteiros

#     for x in lista_final:
#         if indice % 2 != 0:
#             lista_final[indice] = string[indice]
#         indice = indice + 1

# for x in lista_final:
#     print(x, end=" ")

# 7. Para tanto, o programa deverá inicialmente solicitar ao usuário quantos valores serão
# fornecidos para análise e só depois solicitar os valores a serem analisados. A análise
# consistirá em identificar e apresentar a partir da sequência de valores fornecidos, o
# menor valor, o maior valor e a média aritmética dos valores. 

# quantidade_valores = int(input("Quantidade de valores à serem analisados: "))
# numero_elemento = 2
# lista_sequencia = []
# media_valores = 0
# soma_valores = 0

# primeiro_valor = int(input("1º elemento da sequência: "))

# menor_valor = primeiro_valor
# maior_valor = primeiro_valor
# soma_valores += primeiro_valor

# for x in range(quantidade_valores-1):
#     elemento = int(input(f"{numero_elemento}º elemento da sequência: "))
#     numero_elemento += 1
#     soma_valores += elemento
    
#     if elemento > maior_valor:
#         maior_valor = elemento
    
#     elif elemento < menor_valor:
#         menor_valor = elemento
    
# print(f"Menor valor: {menor_valor}\nMaior valor: {maior_valor}\nMédia aritmética: {soma_valores/quantidade_valores:.1f}")


# 8. Escreva um programa que receba como entrada uma string constituída por uma se-
# quência de números inteiros separados por espaço. O programa deverá transformar
# essa string em uma lista de números inteiros e apresentar o resultado da soma dos
# valores das posições ímpares dessa lista.

# entrada = input("Lista de valores inteiros separados por espaço: ")
# lista_valores = []
# indice = 0
# soma_impares = 0

# for x in entrada:
#     if x != " ":
#         lista_valores += [int(x)]

# for y in lista_valores:
#     if indice % 2 == 0:
#         soma_impares += y
#         print(f"+{y}", end="")
#     indice += 1

# print(f'={soma_impares}')

# 9. Escreva um programa que receba como entrada uma string várias palavras separadas
# por espaço. O programa deverá verificar e apresentar a quantidade de ocorrência de
# cada palavra no texto repassado como entrada para o programa. Os sinais de pontu-
# ação não devem ser contabilizados, como por exemplo “.” Ou “,”.

# entrada = input("Várias palavras separadas por espaço: ")
# lista_palavras = []
# palavra = ""
# repetidos = ""

# for x in entrada:
#     if x == "," or x == ".":
#         pass
#     elif x == " ":
#         lista_palavras += [palavra]
#         palavra = ""
#     else:
#         palavra += x

# lista_palavras += [palavra]

# for x in lista_palavras:
#     vezes = 0
#     for y in lista_palavras:
#         if x == y:
#             vezes += 1
#     if vezes > 0:
#         if x in repetidos:
#             pass
#         else:
#             repetidos += f"{x} = {vezes}; "

# print(repetidos)

# MATRIZES (array bidimensional):
# 10. Escreva um programa que leia 9 valores inteiros e armazene em uma matriz 3x3. O
# programa deve informar quantos valores ímpares foram digitados pelo usuário e impri-
# mir a matriz no formato 3x3. Dica: use o operador “%” para verificar se o número é
# ímpar.

# matriz_3x3 = []
# impares = 0

# for x in range(3):
#     linha = []
#     for y in range(3):
#         valor = int(input(f"Digite o valor para a posição ({x+1}, {y+1}): "))
#         linha += [valor]
#         if valor % 2 != 0:
#             impares += 1
#     matriz_3x3 += [linha]

# print(f"Foram digitados {impares} números ímpares.")

# for linha in matriz_3x3:
#     print(linha)

# 11. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
# matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de
# valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
# ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o
# resultado da soma de cada LINHA da matriz.

# linhas = int(input("Digite a quantidade de linhas da matriz: "))
# colunas = int(input("Digite a quantidade de colunas da matriz: "))

# matriz_NxM = []

# for x in range(linhas):
#     soma = 0
#     linha = []
#     for y in range(colunas):
#         valor = int(input(f"Digite o valor para a posição ({x+1}, {y+1}): "))
#         linha += [valor]
#         soma += valor
#     matriz_NxM += [linha] + [(f"Soma da linha = {soma}")]

# # Exibindo a matriz
# for linha in matriz_NxM:
#     print(linha)

# 12. Escreva um programa que solicite ao usuário o valor das duas dimensões de uma
# matriz. Em seguida, solicite ao usuário e armazene nessa matriz uma quantidade de
# valores inteiros correspondente ao tamanho necessário para preencher todas as posi-
# ções da matriz. O programa deverá exibir a matriz de dimensões “m por n” informar o
# resultado da soma de cada COLUNA da matriz. Exemplos:

# 13. Escreva um programa que armazene valores inteiros em duas matrizes A e B de tama-
# nho 3x3. Em seguida gere uma terceira matriz C 3x3 formada pelos maiores valores
# de cada posição comparando as duas primeiras matrizes A e B. 

# 14. Escreva um programa que armazene valores inteiros em uma matrize de tamanho
# 4x4. Em seguida exiba a soma dos elementos que estão em índices de linha ímpar e
# coluna par.

# 15. Escreva um programa que, dada uma matriz de números inteiros aleatórios variando
# entre 100 e 999 de dimensões ‘m’ por ‘n’, ambos podendo variar de 2 a 10, realize os
# seguintes passos: solicite ao usuário as dimensões da matriz; apresente a matriz ge-
# rada de forma aleatória; informe o valor e posição do maior e menor valor na matriz.


# 16. Escreva um programa que realiza o produto matricial entre duas matrizes de dimen-
# sões 3x3. Os valores das duas matrizes devem ser gerados de forma aleatória com
# números inteiros aleatórios variando entre 1 e 9. Ao final, apresente as duas matrizes
# geradas de forma aleatória, bem como a matriz resultante do produto. 

# 17. Escreva um programa que realiza o produto matricial entre duas matrizes de dimen-
# sões ‘j’ por ‘k’ e ‘m’ por ‘n’ fornecidas pelo usuário. Os valores das duas matrizes devem

# ser gerados de forma aleatória com números inteiros aleatórios variando entre dois
# valores, também fornecidos pelo usuário. Ao final, apresente as duas matrizes geradas
# de forma aleatória, bem como a matriz resultante do produto. Caso não seja possível
# realizar o produto matricial, informe a impossibilidade ao usuário e as duas matrizes
# geradas.

# 18. Escreva um programa que leia uma matriz de dimensões 3x6 com valores reais. Em
# seguida, o programa deverá imprimir a soma de todos os elementos das colunas ím-
# pares; imprima a média aritmética dos elementos da segunda e quarta colunas; subs-
# titua os valores da sexta coluna pela soma dos valores das colunas 4 e 5; Exiba a
# matriz modificada e a matriz original.


# lista = [x for x in range(2, 21, 2)]

# for x in range(len(lista)):
#     print(lista[x])