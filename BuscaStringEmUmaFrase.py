# Crie um programa que leia o nome de uma cidade e diga se ela começa
# ou não com o nome "SANTO"

nome_cidade = str(input('Digite aqui o nome da cidade: '))

nome_cidade = nome_cidade.upper()

resultado = nome_cidade.find('SANTO')

if resultado != 0:
    print('O nome da cidade não começa com SANTO')

else:
    print('O nome da cidade começa com SANTO')