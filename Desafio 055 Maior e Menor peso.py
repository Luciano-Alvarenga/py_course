#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

more_weight = 0
minus_weight = 0

for person in range(1, 6):
    weight = float(input(f'Informe o peso da {person}ª pessoa: '))

    if person == 1:
        more_weight = weight
        minus_weight = weight
    else:
        if weight > more_weight:
            more_weight = weight
        if weight < minus_weight:
            minus_weight = weight

print(f'No maior peso foi informado: {more_weight}Kg')
print(f'No menor peso informado: {minus_weight}Kg')
