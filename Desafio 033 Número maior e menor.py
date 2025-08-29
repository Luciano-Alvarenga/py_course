#Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

'''number_1 = float(input('Digite o primeiro valor: '))
number_2 = float(input('Digite o segundo valor: '))
number_3 = float(input('Digite o terceiro valor: '))

maior = max(number_1, number_2, number_3)
menor = min(number_1, number_2, number_3)

print(f'O número maior {maior}')
print(f'O número menor {menor}')'''


number_1 = float(input('Digite o primeiro valor: '))
number_2 = float(input('Digite o segundo valor: '))
number_3 = float(input('Digite o terceiro valor: '))

#Verificando quem é menor.
min = number_1
if number_2<number_1 and number_2<number_3:
    min = number_2
if number_3<number_1 and number_3<number_2:
    min = number_3

#Verificando quem é maior.
max = number_1
if number_2>number_1 and number_2>number_3:
    max = number_2
if number_3>number_1 and number_3>number_2:
    max = number_3

print(f'O maior é {max}')
print(f'O menor é {min}')