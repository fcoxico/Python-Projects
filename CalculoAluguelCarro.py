# Programa para determinar o valor a pagar de um carro alugado

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

valor_km = 0.11111
valor_total = dias * km  * valor_km


print('O total a pagar é de {}'.format(valor_total))