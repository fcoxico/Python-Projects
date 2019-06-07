# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar os espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Insira aqui o seu nome: ')).strip()
nome_separado = nome.split()

x = len(nome)
y = nome_separado[0]


print('Nome maiúsculo - {}'.format(nome.upper()))
print('Nome minúsculo - {}'.format(nome.lower()))
print('O nome tem {} letras'.format(x - nome.count(' ')))
print('O primeiro nome é {} tem {} letras'.format(nome_separado[0], len(y)))


