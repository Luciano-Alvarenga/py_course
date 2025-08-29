#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número:6.127, o número 6.127 tem a parte inteira 6.
import math
num = float(input('Digite um valor: '))
print (f'O valor digitado foi {num} e sua porção inteira é {math.trunc(num)}')