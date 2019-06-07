# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece na primeira vez
# Em que posição ela aparece da última vez


palavra = str(input('Insira aqui uma frase: ')).upper()


print('A letra A aparece {} vezes na frase'.format(palavra.count('A')))
print('A letra A apareceu na primeira vez na posição {}'.format(palavra.find('A')+1))
print('A letra A apareceu na última vez na posição {}'.format(palavra.rfind('A')+1))


