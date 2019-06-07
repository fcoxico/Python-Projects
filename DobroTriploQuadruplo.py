# Escreva um programa que recebe um numero e
# printa o dobro, o triplo e a raiz desse número

n1 = int(input('Insira aqui um número '))

dobro = n1*2
triplo = n1*3
raiz = n1**(1/2)

print('O dobro é {} \n'
      'O triplo é {} \n'
      'A raiz é {} \n'
      .format(dobro, triplo, raiz))
