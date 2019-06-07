# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# dos trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

import random

alunos = input('Insira os nomes dos alunos separados por vírgula: ')

# Retira os espaços antes e depois da vírgula
lista_alunos = alunos.replace(" "," ").split(",")

# Informa o tamanho da lista
tamanho = len(lista_alunos)

# Percorre a lista usando o tamanho como parametro
for i in range(len(lista_alunos)):
    # Retira um elemento da lista de forma aleatória usando o tamanho como parametro
    x = lista_alunos.pop(random.randrange(len(lista_alunos)))
    # Imprime o elemento e também a sua ordem a cada passada do for
    print('O aluno nº {} é {}'.format(i, x))
