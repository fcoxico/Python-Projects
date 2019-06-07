# Faça um programa que leia um número interio qualquer e
# mostre na tela a sua tabuada

n1 = int(input('Insira aqui um número para ver a sua tabuada '))
cont = 1

if n1>=1 and n1 <= 10:
    while cont <=10:
        tab = n1 * cont
        print('{} x {} = {}'.format(n1, cont, tab))
        cont = cont+1

else:
    print('Insira apenas valores de 1 a 10')
