#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex:
# 5! = 5x4x3x2x1 = 120

number = int(input('Digite o número desejado: '))
counter = number
fact = 1
print(f'Calculando {number}! = ', end='')

while counter > 0:
    print (f'{counter}', end='')
    print(' x ' if counter > 1 else ' = ', end='')
    fact *= counter
    counter -= 1

print(f'{fact}')
