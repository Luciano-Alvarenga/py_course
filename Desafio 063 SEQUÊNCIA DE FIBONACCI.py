#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
#SEQUÊNCIA DE FIBONACCI.
#Ex:
# 0 → 1 → 1 → 2 → 3 → 5 → 8

print('=' * 24)
print('SEQUEÊNCIA DE FIBONACCI')
print('=' * 24)

number = int(input('Quantos termos você deseja mostrar?: '))

term_1 = 0
term_2 = 1

print(f'{term_1} → {term_2}', end='')

count = 3
while count <= number:
    term_3 = term_1 + term_2
    print(f' → {term_3}', end='')
    term_1 = term_2
    term_2 = term_3
    count += 1
print(' → FIM')
