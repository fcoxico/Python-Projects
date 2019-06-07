# Crie um programa que leia quanto dinheiro uma pessoa tenha na carteira
# e mostre quantos dolares ela pode comprar

quant_real = float(input('Quanto dinheiro você tem? \n'))

quant_dolar = quant_real / 3.27

print('A quantidade de dolares que você pode comprar é: \n'
      '{:.2f}'.format(quant_dolar))