#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A média de idade do grupo.
#Qual a idade do homem mais velho.
#Quantas mulheres tem menos 20 anos.

from pygame.transform import average_color

total_age = 0
average_age = 0
oldest_man_age = 0
oldest_man_name =''
women_under_20 = 0

for person in range(1, 5):
    print(f'-----{person}ª PESSOA ------')
    name = str(input('Nome: ')).strip()
    age = int(input('Idade: '))
    sex = str(input('Sexo[M/F]: ')).strip().upper()

    total_age += age

    if person == 1 and sex == 'Mm':
        oldest_man_age = age
        oldest_man_name = name
    if sex in 'Mm' and age > oldest_man_age:
        oldest_man_age = age
        oldest_man_name = name

    if sex in 'Ff' and age < 20:
         women_under_20 += 1

average_age = total_age / 4

print(f'A média de idade do grupo é {average_age:.1f} Anos.')
if oldest_man_name:
  print(f'O homem mais velho é {oldest_man_name} com {oldest_man_age} Anos.')
else:
 print('Não há homem no grupo!')
print(f'Ao todo há {women_under_20} mulheres com menos de 20 anos')
