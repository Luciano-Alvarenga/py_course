#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

number = int(input('Digite um número: '))

if number % 2 == 0:
    print(f'Esse número {number} é PAR')

else:
    print(f'Esse número {number} é IMPAR')