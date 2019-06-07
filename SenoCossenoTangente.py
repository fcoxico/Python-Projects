 #Faça um programa que leia um ângulo qualquer e mostre na tela o valor
 # do seno, do cosseno e da tanguente desse ângulo


from math import sin, cos, tan

angulo = int(input('Insira o valor do angulo que você quer saber: '))



print(50*'-')
print('O valor do Seno é {:.2f}:'.format(sin(angulo)))
print(50*'-')
print('O valor do Cosseno é {:.2f}:'.format(cos(angulo)))
print(50*'-')
print('O valor da Tangente é {:.2f}:'.format(tan(angulo)))
