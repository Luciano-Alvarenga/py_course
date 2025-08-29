print('-=-' * 28)
print('Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')
print('-=-' * 28)
n = int(input('Digite um valor: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print (f'O dobro de {n} vale {d}.')
print (f'O triplo de {n} vale {t}. \nA raiz quadrada de {n} vale {r:.0f}.')
#Importando a biblioteca math(matemática)
from math import sqrt
num = int(input('Digite um valor: '))
n1 = num * 2
n2 = num * 3
n3 = (sqrt(num))
print (f'O dobro de {num} vale {n1}.')
print(f'O triplo de {num} vale {n2}.')
print (f'A raiz quadrada de {num} vale {n3:.2f}')