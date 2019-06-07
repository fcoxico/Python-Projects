# Faça um programa que receba um valor em Farenheit e converta para Celsius.

valor_f = float(input("Insira aqui o valor que você quer "
                      "converter de ºF para ºC \n"))

valor_c = (5*(valor_f-32))/9

print('O valor em ºC é {:.2f}'.format(valor_c))
