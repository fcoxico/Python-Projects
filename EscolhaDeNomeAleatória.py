# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# do escolhido

import random


alunos = input('Insira os nomes dos alunos separados por vírgula: ')

# Retira os espaços antes e depois da vírgula
lista_alunos = alunos.replace(" "," ").split(",")


print('O nome do aluno escolhido é {}'.format(random.choice(lista_alunos)))
