# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve 
#mostrar, para cada palavra, quais são as suas vogais.

words = ('canela', 'cadeira', 'arroz', 'carro', 'moto' )

for word in words:
    print(f'\nNa palavra {word.upper()} temos: ', end='')
    for letter in word:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
            
