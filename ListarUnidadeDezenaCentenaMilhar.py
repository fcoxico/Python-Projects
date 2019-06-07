# Faça um programa que leia um numero de 0 a 9999 e mostre na tela
# cada um dos digitos separados por: Unidade, Dezena, Centena e Milhar

valor = int(input('Insira aqui um valor: '))

unidade = int(valor % 10)
dezena = int(((valor % 100)-unidade)/10)
centena = int(((valor % 1000)-dezena-unidade)/100)
milhar = int(((valor % 10000)-centena-dezena-unidade)/1000)

print('O número {} possui:\n'
      '{} unidades\n'
      '{} dezenas\n'
      '{} centenas\n'
      '{} milhares\n'.format(valor, unidade, dezena, centena, milhar))