# Faça um programa que leia o comprimento do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot

cat_oposto = float(input('Digite o valor do Cateto oposto: '))
cat_adjacente = float(input('Digite o valor do Cateto Adjacente: '))

print('O valor da Hipotenusa é: {}'.format(hypot(cat_adjacente,cat_oposto)))