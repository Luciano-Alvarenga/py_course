#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
#atingiram a maioridade e quantas já são maiores.

#Considere 21 anos como maior idade.

from datetime import date

over_age = 0
minors = 0

today = date.today().year

for born_year in range (1, 8 ):

 born_year = int(input(f'Em que ano a {born_year}º pessoa nasceu: '))
 age = today - born_year

 if age >= 21:
     over_age += 1
 else:
    minors += 1

print(f'Ao total tivemos {over_age} pessoas maiores de idade.')
print(f'E também tivemos {minors} pessoas menores de idade.')
