# Faça um programa que leia a largura e altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária parapintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m quadrados


altura = int(input('Qual é o altura da parede: \n'))
largura = int(input('Qual é a largura da parede: \n'))

area_parede = altura * largura

quant_tinta = area_parede/2

if type(quant_tinta) == float:
    quant_tinta = int(quant_tinta)

print('A area de parede é: {}\n'
      'São necessários {} litros para pintar a parede \n'
      .format(area_parede, quant_tinta))