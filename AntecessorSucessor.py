# Recebe um número e depois printa na tela
# o número digitado, o antecessor e o sucessor.


n1 = int(input('Insira aqui um número '))

antes = n1-1
depois = n1+1

print('O número que você digitou foi {} \n'
      'O número que vem antes dele é {} \n'
      'O número que vem depois dele é {} \n '.format(n1, antes, depois))