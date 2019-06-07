# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome_pessoa = str(input('Digite o seu nome: '))
palavra = 'SILVA'

nome_pessoa = nome_pessoa.upper()

if palavra in nome_pessoa:
    print('Possui SILVA no nome')

else:
    print('Não possui SILVA no nome')