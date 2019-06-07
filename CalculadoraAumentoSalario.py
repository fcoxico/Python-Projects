# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo
# salário com 15%  de aumento

salario_atual = float(input('Insira aqui o valor que você ganha atualmente: \n'))

aumento = salario_atual*(15/100)

salario_novo = salario_atual + aumento

print('O salario antigo era de R${:.2f}\n'
      'Você recebeu um aumento de salário de R${:.2f}\n'
      'O novo salário é de R${:.2f}'
      .format(salario_atual, aumento, salario_novo))