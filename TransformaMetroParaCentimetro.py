# Escreva um programa que leia o valor em metros e
# o exiba convertido em centimetros e milimetros

vmetro = float(input('Insira aqui o valor em metros '))

print('O valor em centimetros é {} \n'
      'O valor em milimetros é {} '
      .format(vmetro*100, vmetro*1000))
