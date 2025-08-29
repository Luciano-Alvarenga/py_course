#Escreva um programa que leia 2 números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

number_1 = int(input('Digite um número: '))
number_2 = int(input('Digite outro número: '))

if number_1 > number_2:
    print('O PRIMEIRO número é maior')

elif number_2 > number_1:
    print('O SEGUNDO número é maior!')

else: print('Os dois números são IGUAIS!')