#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

number = int(input('Digite um número: '))
total = 0

for c in range(1, number +1):
    if number % c == 0:
        print('\33[33m', end= ' ')
        total += 1
    else:
        print('\33[31m', end= ' ')
    print(f'{c}', end= '')

print(f'\nO número {number} foi divisivel {total} vezes!')

if total == 2:
    print('E por isso ele É PRIMO.')
else:
    print('Por isso ele NÃO É PRIMO.')
