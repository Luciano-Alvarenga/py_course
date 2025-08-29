#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

#EX:
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATONA

phrase = str(input('Digite o seu nome: ')).strip()

phrase = phrase.upper()
word = phrase.split()
together = ''.join(word)
inverse = ''

for word in range(len(together) -1, -1, -1):
    inverse += together[word]
print(f'O invero {together} é {inverse}.')
if inverse == together:
        print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
