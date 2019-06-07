# Faça um algoritmo que leia o preço de um produto e mostre o seu
# novo preço, com desconto de 5%.

valor_antigo = float(input('Insira aqui o preço antigo do produto: \n'))

desconto = valor_antigo*(5/100)
novo_valor = valor_antigo-desconto

print('O valor antigo era de R${} \n'
      'O valor novo é de R${:.2f} \n'
      'O produto teve um desconto de R${:.2f}\n'
      .format(valor_antigo, novo_valor, desconto))