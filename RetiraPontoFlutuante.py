# Crie um programa que leia um número Real qualquer qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc


num = float(input('Insira aqui um número de ponto flutuante: \n'))

print('O novo número é: {}'.format(trunc(num)))