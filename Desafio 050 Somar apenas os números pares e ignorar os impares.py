#Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares. Se o
#valor digitado for impar, desconsidere-o.

soma = 0
cont = 0

for number in range(1, 7):
 number = int(input(f'Digite o {number}º valor: '))
 if number % 2 == 0:
     soma += number
     cont += 1

print(f'Você informou {cont} números PARES e a soma deles é {soma}')
